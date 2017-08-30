

from sys import stdin


memo = {}

def main():
    line =  stdin.readline().strip()
    while ( line != "0"):
        data = line.split(" ")

        s = [int(x) for x in data]
        r = maxE(s, memo)
        print(r)
        line = stdin.readline().strip()

def maxE(weight, mem):
    #print(weight, " W")
    r = -2
    N = len(weight)

    clave = "-"
    for i in range(N):
        clave += str(weight[i]) + "-"

    if( N == 2):
        r = 0
    else:
        if(N > 2):
            if( clave in memo):

                r = memo[clave]
            else:
                s = weight[:]
                #print(s,"S")

                for i in range (1, N -1):
                    r = max(r,  s[i-1]*s[i+1] + maxE(  modificar(weight, i) , memo) )
                    weight = s[:]
    memo[clave] = r
    return r

def modificar(weigth, i):
    weigth.pop(i)
    return  weigth

main()
