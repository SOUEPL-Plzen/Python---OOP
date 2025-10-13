class person:
    """
    Třída, která slouží k dědičnosti pro zaměstnance a žáky
    """
    def __init__(self, id: int, name: str, surname: str, age: int, gender: str):
        self.id = int(id)
        self.name = str(name)
        self.surname= str(surname)
        self.age = int(age)
        self.gender = str(gender)

# Dědičnost
# student a zaměstnanec bude mít stejné vlastnosti jako person
# student a zaměstnanec bude mít navíc alespoň 2 různé další vlastnosti

class student(person):
    def __init__(self, id: int, name: str, surname: str, age: int, gender: str, fakulty: str, year: int):
        super().__init__(id, name, surname, age, gender)
        self.obor = str(fakulty)
        self.rocnik = int(year)

class employeed(person):
    def __init__(self, id: int, name: str, surname: str, age: int, gender: str, position: str, pay_grade: int):
        super().__init__(id, name, surname, age, gender)
        self.position = str(position)
        self.pay_grade = int(pay_grade)

    def mzda(self, odmeny: float):
        # Základní mzda podle platové třídy
        zakladni_mzdy = {
            10: 25000,
            11: 30000,
            12: 35000,
            13: 40000
        }
        zaklad = zakladni_mzdy.get(self.pay_grade, 25000)
        hruba_mzda = zaklad + odmeny

        # Výpočty srážek
        socialni = hruba_mzda * 0.065
        zdravotni = hruba_mzda * 0.045
        dan = hruba_mzda * 0.15

        cista_mzda = hruba_mzda - socialni - zdravotni - dan

        return {
            "zaklad": zaklad,
            "odmeny": odmeny,
            "hruba_mzda": hruba_mzda,
            "socialni": round(socialni, 2),
            "zdravotni": round(zdravotni, 2),
            "dan": round(dan, 2),
            "cista_mzda": round(cista_mzda, 2)
        }




jan = student(15, "Jan", "Novák", 15, "Kluk", "IT", 1)
Jana = student()

print(jan.name)