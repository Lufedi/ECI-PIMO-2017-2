

def lis(arr):
    n = len(arr)
    #Declarando todos los casos base
    lis = [1] * n
    #Calcular el mejor valor desde abajo hasta el último elemento de la lista (bottom up)
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    maximum = 0

    # Escoger el maximo de todas mejores soluciones
    for i in range(n):
        maximum = max(maximum, lis[i])

    return maximum


arr = [10, 22, 9, 33, 21, 50, 41, 60]
print("Length of LIS is", lis(arr))


arr = [-7, 10, 9, 2, 3, 8, 8, 1]
print("Length of LIS is", lis(arr))
