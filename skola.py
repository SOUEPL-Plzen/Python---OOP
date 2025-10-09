class person:
    def __init__(self, id, name, surname, age, gender):
        self.id = id
        self.name = name
        self.surname= surname
        self.age = age
        self.gender = gender

# Dědičnost
# student a zaměstnanec bude mít stejné vlastnosti jako person
# student a zaměstnanec bude mít navíc alespoň 2 různé další vlastnosti

class student(person):
    def __init__(self, id, name, surname, age, gender, fakulty, year):
        super().__init__(id, name, surname, age, gender)
        self.obor = fakulty
        self.rocnik = year

class employeed(person):
    def __init__(self, id, name, surname, age, gender, position, pay_grade):
        super().__init__(id, name, surname, age, gender)
        self.position = position
        self.pay_grade = pay_grade


jan = student(15, "Jan", "Novák", 15, "Kluk", "IT", 1)

print(jan.name)