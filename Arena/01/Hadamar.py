from sys import stdin
import math


# validar que n sea potencia de 2
def validarPow(n):
    val = math.log(n) / math.log(2)
    if 2 ** val == float(n):
        return True
    else:
        return False


def validarMatriz(m, n):
    cont = 0
    k = 0

    while cont < n - 1:
        cant = validarFilas(m[k:k + n], m[k + n:k + 2 * n])
        k += 4
        cont += 1
        if (cant != n / 2):
            return False

    return True


# encontrar la cantidad de diferencias entre dos filas
def validarFilas(f1, f2):
    cant = 0
    for x in range(len(f1)):
        if (f1[x] != f2[x]):
            cant += 1

    return (cant)


def main():
    n = int(stdin.readline())
    # leer la matriz
    matriz = stdin.readline().strip().split()

    # Validar el caso n=1 y H1=T
    if n == 1:
        if matriz[0] == "T":
            print("Hadamard")
        else:
            print("No Hadamard")
    else:
        # validar si el tamaño es potencia de 2
        if not validarPow(n):
            print("Imposible")
        else:
            if (validarMatriz(matriz, n)):
                print("Hadamard")
            else:
                print("No Hadamard")


main()