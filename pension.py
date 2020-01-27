# PENSION JK & D10S

# Función que devuelva como resultado si una persona cumple con
# los requisitos legales para recibir una pensión de vejez del
# Instituto Venezolano de los Seguros Sociales (IVSS).

# AUTORES:

# David Segura #13-11341
# Jesus Kauze #12-10273

# Funcion que calcule segun edad >= 60 si es H, >= 55 si es mujer,
# acreditadas un minimo de 750 semanas cotizadas

# Funcion que calcule insalubridad, te da derecho a cobrar la pension
# antes de tiempo, se rebaja un año por cada cuatro trabajados un maximo
# de 5 años

# Manejo de fechas mediante liberia de python

def pensionado(sexo,edad,semanas,salubridad):
    limitehombre = 60
    limitemujer = 55
    if salubridad > 0:
        reduccion = salubridad // 4
        if reduccion <= 5:
            if sexo == "h":
                limitehombre -= reduccion
            else:
                limitemujer -= reduccion
        else:
            if sexo == "h":
                limitehombre -= 5
            else:
                limitemujer -= 5
    if sexo == "h" and edad >= limitehombre and semanas >= 750:
        return True
    elif sexo == "m" and edad >= limitemujer and semanas >= 750:
        return True
    else:
        return False