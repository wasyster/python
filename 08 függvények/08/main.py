#A program bekér egy dolgozat pontszámot (x) a felhasználótól
#és kiír egy érdemjegyet az alábbiak szerint! :
# 1: x<50;
# 2: 50<=x<60;
# 3: 60<=x<70;
# 4: 70<=x<85;
# 5: x>=85.

from ast import Return
import os
import time

# hiba
def hiba(uzenet: str) -> None:
    print(uzenet)
    time.sleep(3)
    os.system("cls")

# pontszam bekerese
def pontBekeres()->int:
    pontSzam:int=None
    while(pontSzam==None):
        data:str=input("Kérem a pontszámát: ")
        if(data.isdigit()):
            pontSzam=int(data)
            if (pontSzam >= 0 and pontSzam <= 100):
                return pontSzam
            else:
                pontSzam = None
                hiba("0 és 100 között adjon meg értéket!")
        else:
            hiba("Számot adjon meg!")
                

#pontszam vizsgalata
def vizsgalat (szam: int) -> int:
    if(szam < 50):
        return 1
    elif(szam >= 50 and szam < 60):
        return 2
    elif(szam >=60 and szam < 70):
        return 3
    elif(szam >= 70 and szam < 85):
        return 4
    else:
        return 5

#kiiras
def kiiratas(pontSzam: int, osztalyzat: int)-> None:
    print(f"Ön {pontSzam} pontot ért el, az eredménye pedig {osztalyzat}.")

#foprogram

pontSzam:int = pontBekeres()
osztalyzat:int = vizsgalat(pontSzam)
kiiratas(pontSzam, osztalyzat)
