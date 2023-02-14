from random import *
import string
def Salasona(k: int):
    saladus=""
    for i in range(k):
        t=choice(string.ascii_letters) #Aa...Zz
        num=choice([1,2,3,4,5,6,7,8,9,0])
        sym=choice(["*","-",".","!","_"])
        t_num=[t,str(num),sym]
        saladus+=choice(t_num)
    return saladus

def Registreerimine(l:list,p:list):
    nimi=input("Sisesta oma nimi:")
    v=int(input("1-Ese koostan parooli\n2-Arvuti genireerib\n"))
    if v==1:
        pass
    else:
        salasona=Salasona(5)
        l.append(nimi)
        p.append(salasona)

    return l,p


def Autoriseerimine(l:list,p:list):
    nimi=input("Sisesta oma nimi:")
    salasona=input("Sisesta oma salasõna:")
    if nimi in l:
        ind=l.index(nimi)
        if salasona==p[ind]:
            print("Tere tulemast!")
        else:
            print("Vale salasõna!")
    else:
        print("Nimi ei ole nimekirjas!")























from datetime import *
def date_(d:int, m:int,y:int)-> bool:
    try:
        print(date(y,m,d))
        flag=True
    except :
        flag=False
    return flag






def arithmetic(arv1:float,tehe:str,arv2:float)->any:
    """Kirjuta!!!
    """
    if tehe=="+":
        vastus=arv1+arv2
    elif tehe=="-":
        vastus=arv1-arv2
    elif tehe=="*":
        vastus=arv1*arv2
    elif tehe=="/":
        if arv2==0:
            vastus="DIV0"
        else:
            vastus=arv1/arv2
    else:
        vastus="Tundmatu tehe"

    return vastus

def is_year_leap(aasta: int)->bool:
    """
    """
    if aasta%4==0:
        t=True
    else:
        t=False

    return t


def Sugu(ik_list:list)->str:
    """Esimise tahe järgi määrame sugu
    :param list ik_list: Järjend isikukoodi numbridest
    :rtype: str
    """
    if int(ik_list[0])%2==0:
        sugu="naine"
    else:
        sugu="mees"
    return sugu

def Sunnikoht(a:int)->str:
    """
    """
    if 1<=a<=10:
        haigla="kuresaare Haigla"
    elif 11<=a<=19:
        haigla="Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
    elif 21<=a<=220:
        haigla="Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
    else:
        haigla=" ---"
    return haigla

def Sunnipaev(ik_list:list)->str:
    """
    """
    s1=int(ik_list[0])
    y=ik_list[1]+ik_list[2] #aasta
    m=ik_list[3]+ik_list[4] #kuu
    d=ik_list[5]+ik_list[6] #päev
    if (int(m)<1 or int(m)>13) and (int(d)<1 or int(d)>31):
        spaev="Viga"
        #arvud.append(ik)
    else:
        if s1==1 or s1==2:
            yy="18"
        elif s1==3 or s1==4:
            yy="19"
        else:
            yy="20"
        spaev=d+"."+m+"."+yy+y #ei ole 18..,19..,20..
    return spaev

def naised_mehed(ikoodid:list):
    """...
    :rtype: list
    """
    naised=[]
    mehed=[]
    for kood in ikoodid:
        ik_list=list(kood)
        sugu=Sugu(ik_list)
        if sugu=="naine":
            naised.append(kood)
        else:
            mehed.append(kood)
    ikoodid.clear()
    ikoodid.extend(naised)
    ikoodid.extend(mehed)
    return ikoodid