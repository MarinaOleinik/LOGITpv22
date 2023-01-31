from math import *
from random import *

#31/01/23
#3
arvud=[]
kogus=int(input("Kogus: "))
for i in range(kogus):
    arvud.append(randint(-100,100))
print(arvud)
max_arv=max(arvud)
ind=arvud.index(max_arv)
print(ind)
print(max_arv)
max_arv=max_arv/kogus
arvud.insert(ind,max_arv)
arvud.pop(ind+1)
print(arvud)


#2
maakonnad=["Tln","Narva","K-Järve","Ida-Virumaa","Tartu","Tartumaa","Viljandi","Pärnumaa"]
# tee oma loetelu!
osa1=[]
osa2=[]
print(maakonnad)
if len(maakonnad)%2==0 and len(maakonnad)>=2:
    n=int(len(maakonnad)/2)
    for i in range(1,n+1): #1,...n
        osa1.append(maakonnad[i-1])
    for j in range(n+1,len(maakonnad)+1): #n+1,... len()
        osa2.append(maakonnad[j-1])
    osa1.reverse()
    osa2.reverse()
    osa2.extend(osa1)
    print(osa2)
else:
    print("Viga")




#1
index=""
maakonnad=["Tln","Narva","K-Järve","Ida-Virumaa","Tartu","Tartumaa","Viljandi","Pärnumaa","Saaremaa"]
while True:
    try:
        index=int(input("Anna index: "))
        if index<99999 and index>10000:
            break
    except:
        print("Anna õige index!")
i=index//10000 #1,2,3,4,5,6,7,8,9
print(f"{index} on {maakonnad[i-1]}") #0,1,2,3,4,5,6,7,8
if i in [1,2,3]:
    print()
else:
    print()



#17/01/23
hind=float(input("Vali hind"))
summa=float(input("Anna raha"))
if summa==hind:
    print("Täname ostu eest")
elif summa>hind:
    print(f"Tagasiraha: {summa-hind}")
else:
    print(f"Veel vaja juurde marksta {hind-summa} ")



#16/01/23
#
katsed=0
answer=""
while answer!="komm":
    answer=input("Tahan kommi!")
    katsed+=1
print(f"Katsed: {katsed}")
print()

#11/01/23 Kuusk
for i in range(1,5):
    x=str("*"*i).center(18," ")
    print(x, end="")
    print()
for i in range(1,7):
    x=str("*"*(i+2)).center(18," ")
    print(x, end="")
    print()
for i in range(1,10):
    x=str("*"*(i+4)).center(18," ")
    print(x, end="")
    print()

#09/01/23
#Использование цикла WHILE 

#1)

print("Arvuta peast! ...4*100-55")
o_vastus=4*100-55
vastus=int(input("Lahenda ülesanne ..."))
k=1
while vastus!=o_vastus:
    print("Viga! Sisesta Õige vastus ...", )
    vastus=int(input("Sisesta vastus ..."))
    k+=1
print("Õige vastus! Katsed oli ...",k )
k=1
while True:
    pass

print()

for i in range(2, 12, 3):
    print(i, end=" ")
print()
for i in range(12, 2, -2):
    print(i, end=" ")
print()


#21/12/22
#3
while True:
    try:
        p=float(input("Pikkus: "))
        if p>0: break
    except:
        print("On vaja numbreid kirjutada, mis on suurem kui 0")
while True:
    try:
        l=float(input("Laius: "))
        if l>0: break
    except:
        print("On vaja numbreid kirjutada, mis on suurem kui 0")
while True:
    v=input("Kas tahad remonti teha? ")
    if v.upper()=="JAH" or v.upper()=="EI" : break
if v.upper()=="JAH":
    while True:
        try:
            hind=float(input("Kui palju maksam m^2"))
            break
        except TypeError:
            print()
    hind=l*p*hind
    print(f"Remonti hind on {hind}")
else:
    pass



#2
while True:
    nimi1=input("1. Mis on sinu nimi? ")
    if nimi1.isalpha(): break
while True:
    nimi2=input("2. Mis on sinu nimi? ")
    if nimi2.isalpha(): break
if nimi1=="Anna" and nimi2=="Inna": print("Neid on täna pinginaabrid")





#1
while True:
    nimi=input("Mis on sinu nimi? ")
    if nimi.isalpha(): break
if nimi.upper()=="JUKU":
    while True:
        try:
            vanus=int(input("Kui vana sa oled?"))
            break
        except:
            print("On vaja arvude tüüp kasutada")
    if 0<vanus<6:
        print("Tasuta")
    elif 6<=vanus<=14:
        print("Lastepilet")
    elif 15<=vanus<65:
        print("Täispilet")
    elif 65<=vanus<100:
        print("Sooduspilet")
    else:
        print("Vanus ei soobi!")
else:
    print("Ma otsin Juku!")



print()
#14/12/22
try:
    a=int(input("Sisesta arv"))
    if a>0:
        print("Positiivne")
        if a%2==0:
            print(f"{a} on paaris")
        else:
            print(f"{a} on paaritu")
    else:
        print("Negatiivne")
except:
    print("Vale andmetüüp")

#13/12/22

r=randint(-100,100)
a=randint(-100,100)
print(f"r={r}\na={a}")
if r>0 and a>0:
    pass
else:
    print(f"{a} ja {r} peavad > kui 0 olla")

print()


#12/12/22
print("Nädalapäevad")
try:
    p=int(input("Mis päev täna on?"))
    if p==1:
        n="esmaspäev"
    elif p==2:
        n="teisipäev"
    elif p==3:
        n="kolmapäev"
    elif p==4:
        n="neljapäev"
    elif p==5:
        n="reede"
    elif p==6:
        n="laupäev"
    elif p==7:
        n="pühapäev"
    else:
        n="vale number"
    print(n)  
except:
    print("Viga")







try:
    hinne=int(input("Mis hinne täna said koolis"))
except:
    print("!!!!!!")
if hinne==5:
    print("Väga hea!")
elif hinne==4:
    print("Hea!")
elif hinne==3:
    print("Rahuldav")
elif hinne==2 or hinne==1: #and, or, not, !=ei võrdu, <, >, >=,<=
    print("Mitte rahuldav!")
else:
    print("Viga!")


# 08.12.22
#4
try:
    A1=int(input("Sisesta 1. arv => "))
except:
    print("Vale andmetüüp!")
    A1=0
try:
    A2=int(input("Sisesta 2. arv => "))
except:
    print("Vale andmetüüp!")
    A2=0

A3=int(input("Sisesta 3. arv => "))
A4=int(input("Sisesta 4. arv => "))
A5=int(input("Sisesta 5. arv => "))
Keskmine=(A1+A2+A3+A4+A5)/5
print(f"Keskmine on {Keskmine}")

#6 
a=randint(1,100)
b=randint(1,100)
c=randint(1,100)
print(f"Külg a={a}\nKülg b={b}\nKülg c={c}")
print(f"Kolmnurga ümbermõõt = {a+b+c}")
print()

#1
print("Puu läbimõõdu arvutamine")
C=float(input("Puu ümbermõõt: "))
d=2*(C/(2*pi))
print(f"Vastus:\nPuu läbimõõduga {C} ümbermõõt võrdub {d}")
print()

#2
print("Ristkülikukujulise maatüki diagonaal")
N=float(input("Sisesta ristküliku 1. külje pikkus => "))
M=float(input("Sisesta ristküliku 2. külje pikkus => "))
d=sqrt(N**2+M**2)
print(f"Maatüki diagonaal on {d} m**2")
print()

#3



#5
print("    @..@")
print("   (----)")
print("  ( \__/ )")
print("  ^^ "'""'" ^^ ") 

#-------------------------------
 # 07.12.22
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