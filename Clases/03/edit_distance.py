
def editDistance(str1, str2, m, n):

    #Si la primera cadena es vacia, la unica solucion posible es remover todos los caracteres de la segunda cadena
    if m == 0:
        return n
    # Si la segunda cadena es vacia, la unica solucion posible es remover todos los caracteres de la primera cadena
    if n == 0:
        return m

    #Si ambos caracteres son iguales pasar a la siguiente letra porque no hay que realizar ninguna operacion
    if str1[m - 1] == str2[n - 1]:
        return editDistance(str1, str2, m - 1, n - 1)

    # Si el ultimo caracter no es igual, ejecutar las 3 posibles operaciones
    #Y tomar el minimo valor de las 3 opciones
    return 1 + min(editDistance(str1, str2, m, n - 1),  # Inertar
                   editDistance(str1, str2, m - 1, n),  # Remover
                   editDistance(str1, str2, m - 1, n - 1)  # Reemplazar
                   )


str1 = "algorithms"
str2 = "algo"
print (editDistance(str1, str2, len(str1), len(str2)))

# This code is contributed by Bhavya Jain