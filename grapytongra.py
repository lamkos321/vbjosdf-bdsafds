
MAKS_WAGA = 50
zloto = 50

ekwipunek = {
    "miecz": {"ilosc": 1, "waga": 5, "wartosc": 30},
    "mikstura": {"ilosc": 3, "waga": 1, "wartosc": 10}
}


def pokaz_wage():
    waga = 0

    for nazwa in ekwipunek:
        waga += ekwipunek[nazwa]["waga"] * ekwipunek[nazwa]["ilosc"]

    print("Waga:", waga, "/", MAKS_WAGA)


def pokaz_zloto():
    print("Zloto:", zloto)


def pokaz_przedmioty():
    print("\n--- EKWIPUNEK ---")

    if len(ekwipunek) == 0:
        print("Ekwipunek jest pusty")

    for nazwa in ekwipunek:
        print(nazwa, "x", ekwipunek[nazwa]["ilosc"])

    pokaz_wage()
    pokaz_zloto()


def dodaj_przedmiot():
    global zloto

    print("\n--- SKLEP ---")
    print("tarcza - waga: 6, cena: 25")
    print("luk - waga: 3, cena: 40")
    print("strzaly - waga: 1, cena: 2")
    print("helm - waga: 4, cena: 20")
    print("zbroja - waga: 12, cena: 80")
    print("chleb - waga: 1, cena: 3")
    print("mikstura - waga: 1, cena: 10")

    nazwa = input("Co chcesz kupic? ").lower()

    if nazwa == "tarcza":
        waga = 6
        cena = 25
    elif nazwa == "luk":
        waga = 3
        cena = 40
    elif nazwa == "strzaly":
        waga = 1
        cena = 2
    elif nazwa == "helm":
        waga = 4
        cena = 20
    elif nazwa == "zbroja":
        waga = 12
        cena = 80
    elif nazwa == "chleb":
        waga = 1
        cena = 3
    elif nazwa == "mikstura":
        waga = 1
        cena = 10
    else:
        print("Nie ma takiego przedmiotu")
        return

    ile = int(input("Ile sztuk? "))

    if ile <= 0:
        print("Nieprawidlowa ilosc")
        return

    koszt = cena * ile
    dodatkowa_waga = waga * ile

    aktualna_waga = 0

    for przedmiot in ekwipunek:
        aktualna_waga += ekwipunek[przedmiot]["waga"] * ekwipunek[przedmiot]["ilosc"]

    if zloto < koszt:
        print("Masz za malo zlota")
        return

    if aktualna_waga + dodatkowa_waga > MAKS_WAGA:
        print("Za duza waga")
        return

    zloto -= koszt

    if nazwa in ekwipunek:
        ekwipunek[nazwa]["ilosc"] += ile
    else:
        ekwipunek[nazwa] = {
            "ilosc": ile,
            "waga": waga,
            "wartosc": cena
        }

    print("Kupiono:", nazwa, "x", ile)


def uzyj_przedmiotu():
    nazwa = input("Ktory przedmiot chcesz uzyc? ").lower()

    if nazwa not in ekwipunek:
        print("Nie masz tego przedmiotu")
        return

    ekwipunek[nazwa]["ilosc"] -= 1

    print("Uzyto:", nazwa)

    if ekwipunek[nazwa]["ilosc"] == 0:
        del ekwipunek[nazwa]


def sprawdz_przedmiot():
    nazwa = input("Jaki przedmiot sprawdzic? ").lower()

    if nazwa in ekwipunek:
        print("Ilosc:", ekwipunek[nazwa]["ilosc"])
        print("Waga:", ekwipunek[nazwa]["waga"])
        print("Wartosc:", ekwipunek[nazwa]["wartosc"])
    else:
        print("Nie masz tego przedmiotu")


def menu():
    while True:
        print("\n--- MENU BOHATERA ---")
        print("1. Pokaż przedmioty")
        print("2. Dodaj przedmiot")
        print("3. Użyj przedmiotu")
        print("4. Sprawdź przedmiot")
        print("5. Wyjdź")

        wybor = input("Wybierz: ")

        if wybor == "1":
            pokaz_przedmioty()
        elif wybor == "2":
            dodaj_przedmiot()
        elif wybor == "3":
            uzyj_przedmiotu()
        elif wybor == "4":
            sprawdz_przedmiot()
        elif wybor == "5":
            print("Do zobaczenia!")
            break
        else:
            print("Nieprawidłowy wybór")


menu()
