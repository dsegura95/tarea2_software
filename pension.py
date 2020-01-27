# PENSION JK & D10S

# Función que devuelva como resultado si una persona cumple con
# los requisitos legales para recibir una pensión de vejez del
# Instituto Venezolano de los Seguros Sociales (IVSS).

# AUTORES:

# David Segura #13-11341
# Jesus Kauze #12-10273

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