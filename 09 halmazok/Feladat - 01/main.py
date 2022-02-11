"""
Töltsünk fel egy listát a felhasználó által megadott elemű random számokkal:
"""

from typing import *
import random
import time
import os

halmaz: List[int] = []
elemekSzama: int = None

def hiba(uzenet: str) -> None:
    print(uzenet)
    time.sleep(3)
    os.system("cls")

def elemSzamBekerese() -> int:
    eredmeny: int = None
    
    while(eredmeny == None or eredmeny < 2):
        temp: str = input("Kérem adja meg a halmaz elemeine a számát: ")

        if(temp.isdigit()):
            eredmeny = int(temp)

            if(eredmeny < 2):
                hiba("A halmaz ellemeinek száma legalább kettőnek kell, hogy legyen")
        else:
            hiba("Nem számot adott meg")
            
    return eredmeny

#foprogram
elemekSzama = elemSzamBekerese()