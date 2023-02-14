from OmaModul import *
p=["12345"]
l=["Python"]

while True:
    print(l)
    print(p)
    v=int(input("1-Registreerimine\n2-Aurotiseerimine\n3-Välja\n"))
    if v==1:
        l,p=Registreerimine(l,p)
        pass
    elif v==2:
        Autoriseerimine(l,p)
    elif v==3:
        break
    else:
        print("Tee õige valik")
