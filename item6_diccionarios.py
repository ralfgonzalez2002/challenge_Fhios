'''Concatenar dos diccionarios'''

meses1 = {1:"Ene", 2:"Feb", 3:"Mar", 4:"Abr", 5:"May", 6:"Jun"}
meses2 = {7:"Jul", 8:"Ago", 9:"Sep", 10:"Oct", 11:"Nov", 12:"Dic"}
meses3 = {}

def conca_Diccionarios1(dic1, dic2):
    dic1.update(dic2)
    return (print(dic1))


def conca_Diccionarios2(dic1, dic2):
    dic3 = dic1 | dic2
    return (print(dic3))


conca_Diccionarios1(meses1, meses2)
conca_Diccionarios2(meses1, meses2)