'''Concatenar dos listas'''
lista_A = ["Ene","Feb","Mar","Abr","May","Jun"]
lista_B = ["Jul","Ago","Sep","Oct","Nov","Dic"]
lista_C =[]

def conca_Listas(lista_A, lista_B):
    lista_C = lista_A + lista_B
    return print(lista_C)


def conca_Listas2(lista_A, lista_B):
    lista_A.extend(lista_B)
    return print(lista_A)


conca_Listas(lista_A, lista_B)
conca_Listas2(lista_A, lista_B)