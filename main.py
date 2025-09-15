class car:
    znacka = "" 

    def __init__(self, znacka):
        self.znacka = znacka

audi = car("Audi") #Instance
skoda = car("Škoda")

print(audi.znacka)
print(skoda.znacka)