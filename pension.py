# PENSION JK & D10S

# Función que devuelva como resultado si una persona cumple con
# los requisitos legales para recibir una pensión de vejez del
# Instituto Venezolano de los Seguros Sociales (IVSS).

# AUTORES:

# David Segura #13-11341
# Jesus Kauze #12-10273

# Manejo de fechas mediante liberia de python
# Imports
import datetime

# Manejo de fechas mediante liberia de python


# Funcion para calcular la edad, Parametros: Fecha de nacimiento

def CalcularEdad(nacimiento):
    hoy = datetime.date.today()

    # Edad Negativa por fecha futura
    if hoy < nacimiento:
        print('Fecha de nacimiento Invalida')
    elif (hoy.year - nacimiento.year)  > 140:
        print('La Fecha proporcionada supera los 140 anos de edad, Por favor verifique e ingrese nuevamente')
    else:
        ano = nacimiento.year
        mes = nacimiento.month
        dia = nacimiento.day
        fecha = nacimiento
        edad = 0
        while fecha < hoy:
            edad += 1
            fecha = datetime.date(ano+edad, mes, dia)

        # print('Mi edad es: %s' % (edad-1))
        return edad-1

