#přidání náhodných čísel
import random

#vytvoření 1. pole
arraya = [42, 3, 79, 96, 21, 10, 66, 72, 43, 57]

#výměna indexu 5
arraya[5] = 34

#vypsání zadaných indexů
print(arraya[0])
print(arraya[4])
print(arraya[9])

#vypsání 7. indexu
print(arraya[7])

#vypsání délky pole
print(len(arraya))

#vypsání max. a min. hodnoty
print(max(arraya))
print(min(arraya))

#vytvoření 2. pole
arrayb = [4, 59, 61, 7, 120, 36, 98, 12, 3]

#sečtení polí
print(sum(arraya + arrayb))

#sečtení 1. a 5. indexu z 2. pole
print(arrayb[1] + arrayb[5])

#bonus-randomizace 2. pole
random.shuffle(arrayb)
print (arrayb)