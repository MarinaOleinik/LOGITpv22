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