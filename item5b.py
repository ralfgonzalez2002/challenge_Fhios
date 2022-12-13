'''Un oficial de correos decide optimizar el trabajo de su oficina cortando todas las
palabras de más de cinco letras a sólo cinco letras (e indicando que una palabra fue
cortada con el agregado de una arroba). Además, elimina todos los espacios en blanco
de más.
b) Los puntos se reemplazan por la palabra especial "STOP", y el punto final (que
puede faltar en el texto original) se indica como "STOPSTOP"
ej. texto: " Llego mañana. Voy a almorzar " Se lo transcribe como: "Llego
mañan@ STOP Voy a almor@ STOPSTOP".'''

def corta_palabras(texto, max_char):
    texto_nuevo =""
    lista = texto.split(" ")
    lista_actualizada = []
    for i in range(len(lista)):
        if lista[i][-1] == "." and i != len(lista) - 1:
            lista_actualizada.append(lista[i][:-max_char] + "@")
            lista_actualizada.append(lista[i][-1].replace(".", " STOP"))

        elif lista[i][-1] == "." and i == len(lista) - 1:
            lista_actualizada.append(lista[i][:-max_char] + "@")
            lista_actualizada.append(lista[i][-1].replace(".", " STOPSTOP"))

        elif len(lista[i]) > max_char:
            if lista[i][-1] == ".":
                lista[i][-1].replace(".", )
            lista_actualizada.append(lista[i][:-max_char] + "@")

        elif len(lista[i]) <= max_char:
            lista_actualizada.append(lista[i])

    for j in lista_actualizada:
        texto_nuevo += j + " "
    return print(texto_nuevo)


corta_palabras("Desafio larguisimo. Dias de muchisimo trabajo.", 4)