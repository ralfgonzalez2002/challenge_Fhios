'''Escribir una función “diaSiguienteB” que dada una fecha expresada como la terna (Día,
Mes, Año) (donde Día y Año son números enteros, y Mes es el texto "Ene", "Feb", . . .,
"Dic", según corresponda) calcule el día siguiente al dado, en el mismo formato.'''


def diaSiguienteA(dia, mes, anio):
    meses = {1:"Ene", 2:"Feb", 3:"Mar", 4:"Abr", 5:"May", 6:"Jun", 7:"Jul", 8:"Ago", 9:"Sep", 10:"Oct", 11:"Nov",
             12:"Dic"}
    bisiesto = False

    if anio % 400 == 0:
        bisiesto = True
    elif anio % 4 == 0:
        bisiesto = True

    if mes in meses.get(1 or 3 or 5 or 7 or 8 or 10 or 12):
        dias_mes = 31
    elif mes == meses.get(2):
        if bisiesto:
            dias_mes = 29
        else:
            dias_mes = 28
    else:
        dias_mes = 30

    if dia < dias_mes:
        dia += 1
    else:
        dia = 1
        if mes == meses.get(12):
            mes = meses.get(1)
            anio += 1
        else:
            for i in meses:

                if mes == meses[i]:
                    mes = meses[i + 1]
                    break
    return (dia, str(mes), anio)

print(diaSiguienteA(28, "Feb", 2011))