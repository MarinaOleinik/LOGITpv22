from math import *
#1
print("Puu läbimõõdu arvutamine")
C=float(input("Puu ümbermõõt: "))
d=2*(C/(2*pi))
print(f"Vastus:\nPuu läbimõõduga {C} ümbermõõt võrdub {d}")

#2
print("Ristkülikukujulise maatüki diagonaal")
N=float(input("Sisesta ristküliku 1. külje pikkus => "))
M=float(input("Sisesta ristküliku 2. külje pikkus => "))
d=sqrt(N**2+M**2)
print(f"Maatüki diagonaal on {d} m**2")

#3





#--------------------------------
 
print()
print("Ruudu karakteristikud")
a=float(input("Sisesta ruudu külje pikkus => "))
S=a**2
print("Ruudu pindala", round(S,1))
P=4*a
print("Ruudu ümbermõõt", round(P,1))
di=a*sqrt(2)
print("Ruudu diagonaal", round(di,2))
print()
#-----------------------------
print("Ristküliku karakteristikud")
b=float(input("Sisesta ristküliku 1. külje pikkus => "))
c=float(input("Sisesta ristküliku 2. külje pikkus => "))
S=b*c
print("Ristküliku pindala", round(S,1))
P=2*(b+c)
print("Ristküliku ümbermõõt", round(P,1))
di=sqrt(b*2+c*2)
print("Ristküliku diagonaal", round(di,1))
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => "))
d=2*r
print("Ringi läbimõõt", round(d,1))
S=pi*r**2
print("Ringi pindala", round(S,2))
C=2*pi*r
print("Ringjoone pikkus", round(C,2))

#----------------------------------------------
from math import * #*-kõik funktsioonid on vaja kasutada. kasutame: sin()

#import math kasutame: math.sin()
#2.osa Math kasutamine 
print("Ristküliku ja ringi pindalad")
a=float(input("Anna laius: "))
b=float(input("Anna kõrgus: "))
S=a*b #+,-,/,*,**,sqrt(),//,%
d=sqrt(a**2+b**2)
r=float(input("Anna raadius: "))
Skr=pi*r**2
print(f"Ristküliku pindala on {S}. Ringi pindala on {round(Skr,2)}.")




#1.osa print(), input(),int(),float()
print("Tere tulemast!") #print() teksti või andmete väljastuseks
nimi=input("Mis on sinu nimi? ")#Sisendi lugemine: akraanil "..."ja ootab , kuni kasutaja vajutab Enter klahvi
# input() -> str
print(f"{nimi}, sul on väga ilus nimi!")
print(nimi,", sul on väga ilus nimi!")#kui on erinevat andmete tüübid
print(nimi+", sul on väga ilus nimi!")#kui on sarnane andmete tüüp
vanus=int(input("Kui vana sa oled? "))# input()->int
print(f"{nimi} jargmisel aastal saad {vanus+1}")#muutuja vanus ei muuda
print("Aga selle aastal on ", vanus)
vanus+=1 #muudame muutuja väärtus
print(f"Järgmine aasta on käes, siis {nimi} on {vanus} aastat vana")
pikkus=float(input("Mis on sinu pikkus? ")) #input()->float: 1.75
print(f"{nimi} on {vanus} aastat vana ja suurepärase pikkusega {pikkus}")