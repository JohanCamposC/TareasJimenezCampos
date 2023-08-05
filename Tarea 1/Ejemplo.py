
def Ordena_lista(lista):   # Función para ordenar los numeros de una lista
    n=len(lista)           # Asigna a n el tamaño de la lista

    for i in range(n-1):

        # Se recorre el ciclo la cantidad de datos en la lista menos uno,
        # para pasar por todos los datos de la lista menos el ultimo que se                         
        # Se acomoda por descarte

        for j in range(0, n - i - 1):  # Ciclo para comparar los numeros con el siguiente

            if lista[j] > lista[j + 1]:  # Valida si actual es mayor al siguiente
                lista[j], lista[j + 1] = lista[j + 1], lista[j]   # Reacomodo 


numeros = [5, -7, 3, 58, 14]
print("Números originales:",numeros)
Ordena_lista(numeros)
print("Números ordenados:", numeros)
