'''Esc2ribir una función “diaSiguienteA” que dada una fecha expresada como la terna (Día,
Mes, Año) (donde Día, Mes y Año son números enteros) calcule el día siguiente al dado,
en el mismo formato.'''

def diaSiguienteA(dia, mes, anio):
    meses = {1:"Ene", 2:"Feb", 3:"Mar", 4:"Abr", 5:"May", 6:"Jun", 7:"Jul", 8:"Ago", 9:"Sep", 10:"Oct", 11:"Nov",
             12:"Dic"}
    bisiesto = False

    if anio % 400 == 0:
        bisiesto = True
    elif anio % 4 == 0:
        bisiesto = True

    if mes in (1, 3, 5, 7, 8, 10, 12):
        dias_mes = 31
    elif mes == 2:
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
        if mes == 12:
            mes = 1
            anio += 1
        else:
            mes += 1
    return (dia, meses.get(mes), anio)


print(diaSiguienteA(28, 2, 2022))