'''Concatenar dos tuplas'''

lista_A = ("Lun","Mar","Mie")
lista_B = ("Jue","Vie","Sab","Dom")
lista_C =[]

def conca_Tuplas(lista_A, lista_B):
    lista_C = lista_A + lista_B
    return print(lista_C)

conca_Tuplas(lista_A, lista_B)