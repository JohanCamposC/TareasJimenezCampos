# Para esta función se hace la separación de las minusculas y mayusculas de
# una cadena de caracteres
# Se realizan una serie de validaciones para poder realizar este función

def separa_letras(Cadena):

    mayusculas = ""  # Se definen las variables de salida
    minusculas = ""
    mensaje = ""

    if isinstance(Cadena, str):  # Verifica si la variable es de tipo string

        if Cadena != "":  # Verifica que no sea un string vacio

            if Cadena.isalpha():  # Valida si el caracter es del abecedario

                for caracter in Cadena:  # Separa en minusculas y mayusculas

                    if caracter.isupper():
                        mayusculas += caracter

                    elif caracter.islower():
                        minusculas += caracter

                mensaje = 0  # Mensaje de exito
            else:  # Error caracteres que no esten dentro de abecedario
                mensaje = -200
                mayusculas = None
                minusculas = None

        else:  # Error en caso de que sea un string vacio
            mensaje = -300
            mayusculas = None
            minusculas = None
    else:  # Error en caso de no ser variable tipo string
        mensaje = -100
        mayusculas = None
        minusculas = None


# Devuelve valores, string con mayusculas, minusculas y si fue existoso o no

    return mensaje, mayusculas, minusculas

# Para esta función se ingresa el número de base y número potencia deseados
# para el cálculo de potencia. El código verificará que los valores ingresados
# sean de tipo int.


def potencia_manual(base, potencia):

    if not isinstance(base, int):  # El valor de base no es int

        Estado = -400
        return Estado, None

    elif not isinstance(potencia, int):  # El valor de potencia no es int

        Estado = -400
        return Estado, None

    elif base == 1 or potencia == 0:  # Caso especial de potencia

        return 0, 1

    else:

        Estado = 0  # No hay errores ni casos especiales

# Se inician las condiciones iniciales

    result = 0  # Variable que tendrá el resultado final
    op = 0  # Variable que auxiliar
    suma = base  # Resultado de la 'multiplicación anterior'


# El ciclo for simula la cantidad de multiplicaciones necesarias para la
# potencia (son potencia-1 multiplicaciones). El segundo ciclo for Simula
# cada multiplicación: primero sería base*base=suma, luego sería
# suma*base= suma2 y así por todo el ciclo for

    for i in range(potencia-1):

        for j in range(base):

            op = suma + op

        suma = op
        op = 0

    result = suma

# Primero se devuelve el estado(si hubo error) y segundo el resultado

    return Estado, result
