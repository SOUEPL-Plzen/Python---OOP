class car:
    """
    Zadejte základní parametry auta
    \nCenu auta udáváme v DPH
    """

    
    # Je možnost, kontrolovat si vstupní datové typy, které příjdou při instanci do objektu.
    # Zamezíme tím případným potížím.
    def __init__(self, znacka: str, rok: int, model: str, barva: str,typ_prevodovky: str, cena: float):
        self.znacka = znacka
        self.rok = rok
        self.model = model
        self.barva = barva
        self.typ_prevodovky = typ_prevodovky
        self.cena = cena

    def cena_bez_dph(self):
        """ Vypočítá cenu auta bez DPH"""
        return f" {self.cena * 0.79} kč"

    def vypis(self):
        """ Vypíše základní informace o autu"""
        return f"Název auta: {self.znacka} \nRok výroby: {self.rok} \nModel: {self.model} \nBarva: {self.barva} \n Typ převodovky: {self.typ_prevodovky} \n Cena včetně DPH: {self.cena} Kč, \n Cena bez DPH: {self.cena_bez_dph()}"

    def priplatkova_vybava(self, vybava: str, cena_vybavy: float):
        """ Přidá příplatkovou výbavu k autu"""
        return f"Připlatková výbava: {vybava}, cena příplatkové výbavy je: {cena_vybavy} Kč, celková cena auta s příplatkovou výbavou je: {self.cena + cena_vybavy} Kč"

audi = car("Audi", "aaaa","A4", "stříbrná", "Manuální", 45000) #Instance
skoda = car("Škoda", 2014, "Superb II", "Bílá", "Manuální", 310000)

print(audi.rok)
print(skoda.model)
print(audi.vypis())
print(f"Cena auta bez DPH je: {audi.cena_bez_dph()}")
print(skoda.priplatkova_vybava("metalíza", 15000))
