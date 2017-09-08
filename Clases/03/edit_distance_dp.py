
def editDistDP(str1, str2, m, n):

    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    # Tabulacion
    for i in range(m + 1):
        for j in range(n + 1):

            # Si la primera cadena es vacia, la unica solucion posible es remover todos los caracteres de la segunda cadena
            if i == 0:
                dp[i][j] = j
            # Si la segunda cadena es vacia, la unica solucion posible es remover todos los caracteres de la primera cadenag
            elif j == 0:
                dp[i][j] = i

            # Si ambos caracteres son iguales pasar a la siguiente letra porque no hay que realizar ninguna operacion
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]


            # Si el ultimo caracter no es igual, ejecutar las 3 posibles operaciones
            # Y tomar el minimo valor de las 3 opciones
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],  # Insertar
                                   dp[i - 1][j],  # Remover
                                   dp[i - 1][j - 1])  # Reemplazar

    return dp[m][n]


str1 = "algorithms"
str2 = "algo"

print(editDistDP(str1, str2, len(str1), len(str2)))
