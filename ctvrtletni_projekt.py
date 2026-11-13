import random 
import sys

def cas(cas_navic):
    zaklad = 65
    vysledek = zaklad + cas_navic
    print("")
    print(f"Gratulace, přežil jsi! Tvůj celkový čas je {vysledek}s.")

cas_navic = 0
def dotaz (otazka, moznosti):
    while True:
        odpoved = input(otazka).lower().strip()
        if odpoved in moznosti:
            return odpoved
        else:
            print("mas tam chybu")

def vyber():
    print("Chystáš se na nejtěžší trail na světě, ale nejdříve si musíš připravit kolo.")
    kolo = ["pevné ráfky, ale těžké (napiš 1)", "lehčí ráfky, ale křehčí (napiš 2)", "brzdy, které dobře brzdí v suchu, ale když se namočí, moc nebrzdí (napiš 3)", "brzdy, které brzdí tak průměrně v mokru i v suchu (napiš 4)"]
    for komponenta in kolo:
        print(komponenta)
    while True:
        print("Napiš číslo pro vybrání komponent (vyber jedny brzdy a jedny ráfky).")
        nastaveni = input("Zadej čísla komponent (1-4) a odděl je čárkou: ").strip()
        rozdeleni = nastaveni.split(",")
        if len(rozdeleni) != 2:
            print("Máš buď moc, nebo moc málo čísel.")
            continue
        else:
            try:
                cislo1 = int(rozdeleni[0])
                cislo2 = int(rozdeleni[1])
            except ValueError:
                print("Napiš číslo, ne písmeno.")
                continue
            if cislo1 == cislo2:
                print("Čísla se musí lišit.")
                continue
            elif cislo1 < 0 or cislo2 < 0:
                print ("zadej vyšší číslo")
                continue
            elif cislo1 > 4 or cislo1 < 1 or cislo2 > 4 or cislo2 < 1:
                print("Zadej nižší číslo nebo přidej čárku.")
                continue
            elif (cislo1 <= 2 and cislo2 <= 2) or (cislo1 >= 3 and cislo2 >= 3):
                print("Musíš vybrat od každého jedno.")
                continue
            else:
                komponenty = []
                if cislo1 == 1 or cislo2 == 1:
                    komponenty.append("pevne_rafky")
                if cislo1 == 2 or cislo2 == 2:
                    komponenty.append("lehke_rafky")
                if cislo1 == 3 or cislo2 == 3:
                    komponenty.append("silne_brzdy")
                if cislo1 == 4 or cislo2 == 4:
                    komponenty.append("spolehlive_brzdy")
        return komponenty
def vypis():
    if "pevne_rafky" in komponenty:
        print("Vybral sis pevné ráfky, ale těžké.")
    if "lehke_rafky" in komponenty:
        print("Vybral sis lehčí ráfky, ale křehčí.")
    if "silne_brzdy" in komponenty:
        print("Vybral sis brzdy, které dobře brzdí v suchu, ale když se namočí, moc nebrzdí.")
    if "spolehlive_brzdy" in komponenty:
        print("Vybral sis brzdy, které brzdí tak průměrně v mokru i v suchu.")

def skok_1():
    print("Vyjel jsi a je před tebou první skok.")
    otazka = "Objedeš ho a budeš o 1s pomalejší, nebo ho skočíš? Čas se ti nezdelší, ale je riziko, že nedoletíš a zdelšíš si to o 2s. Odpověz slovem |skocit| nebo |objet|: "
    volba = dotaz(otazka, ["skocit", "objet"])
    if volba == "skocit":
        sance1 = random.randint(1, 100)
        if sance1 < 31:
            print("Nedoletěl jsi, máš 2s navíc.")
            return 2
        else:
            print("Dal jsi to čistě.")
            return 0
    else:
        print("Objel jsi to (+1s).")
        return 1

def drop():
    print("Jedeš dál a je před tebou drop.")
    otazka = "Jdeš váhou |dozadu| nebo |dopredu|? Jestli dopředu, žádné riziko, ale máš +2s. Když jdeš dozadu, můžeš to mít rychlejší, ale máš šanci, že ti praskne ráfek: "
    volba = dotaz (otazka, ["dozadu", "dopredu"])
    if volba == "dozadu":
        sance2 = random.randint(1, 100)
        if "pevne_rafky" in komponenty:
            if sance2 < 31:
                print("Praskl ti ráfek, končíš.")
                sys.exit()
            else:
                print("Čistý dolet.")
                return 0
        elif "lehke_rafky" in komponenty:
            if sance2 < 61:
                print("Praskl ti ráfek, končíš.")
                sys.exit()
            else:
                print("Čistý dolet.")
                return 0
            return 0
    else:
        print("Dobrý (+2s).")
        return 2

def smula ():
    nahoda1 = random.randint(1, 5)
    if nahoda1 == 3:
        print("Najel jsi do louže a máš mokré celé kolo.")
    return nahoda1
    
def kameny():
    print("Stále pokračuješ a vidíš před sebou kamennou sekci.")
    otazka = "Pojedeš co nejrychleji, ale po špičatých kamenech, které ti můžou zničit ráfek (napiš |ostre|), nebo pojedeš přes větší a méně nebezpečné kameny, ale zdelšíš si čas o 2s (napiš |tupe|)? "
    volba = dotaz (otazka, ["ostre", "tupe"])
    if volba == "ostre":
        sance3 = random.randint(1, 1000)
        if "pevne_rafky" in komponenty:
            if sance3 < 301:
                print("Praskl ti ráfek, končíš.")
                sys.exit()
            else:
                print("Přežil jsi to.")
                return 0
        elif "lehke_rafky" in komponenty:
            if sance3 < 701:
                print("Praskl ti ráfek, končíš.")
                sys.exit()
            else:
                print("Přežil jsi to.")
                return 0
    else:
        print("Dobrý (+2s).")
        return 2
    
def nahoda():
    nahoda2 = random.randint(1, 5)
    zmena = 0
    if nahoda2 < 4:
        print("Spadl ti do cesty kámen.")
        if nahoda1 == 3: 
            if "silne_brzdy" in komponenty:
                print("Neubrzdil jsi to, naboural jsi a rozbil ses.")
                sys.exit()
            else: 
                print("Brzdy tě zachránily, ale máš o 4s delší čas.")
                zmena += 4
        else:
            print("Díky dobrým brzdám jsi to stihl perfektně zabrzdit a zdelšil sis čas jen o 1s.")
            zmena += 1
    if "lehke_rafky" in komponenty:
        print ("Díky lehkým ráfkům jsi jel rychle a zkrátil jsi čas o 2s")
        zmena -= 2
    return zmena
    
komponenty = vyber() 
print ("")
vypis()
print ("")
cas_navic += skok_1()
print ("")
cas_navic += drop()
print ("")
nahoda1 = smula()
print ("")
cas_navic += kameny()
print ("")
cas_navic += nahoda()
print ("")
cas(cas_navic)
