'''Un oficial de correos decide optimizar el trabajo de su oficina cortando todas las
palabras de más de cinco letras a sólo cinco letras (e indicando que una palabra fue
cortada con el agregado de una arroba). Además, elimina todos los espacios en blanco
de más.
a) Escribir una función que reciba un texto, la longitud máxima de las palabras y
devuelva como resultado el texto del telegrama.
Ej. texto " Llego por la mañana alrededor del mediodía, esperame para cenar "
se transcribe como "Llego por la mañan@ alred@ del medio@ esper@ para cenar".'''

def corta_palabras(texto, max_char):
    texto_nuevo =""
    lista = texto.split(" ")
    lista_actualizada = []
    for i in range(len(lista)):
        if len(lista[i]) > max_char:
            lista_actualizada.append(lista[i][:max_char] + "@")
        else:
            lista_actualizada.append(lista[i])
    for j in lista_actualizada:
        texto_nuevo += j + " "
    return print(texto_nuevo)


corta_palabras("Estoy de vacaciones y volveré la próxima semana", 5)