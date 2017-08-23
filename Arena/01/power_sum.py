
from sys import stdin


count = 0

def main():
    n = int(stdin.readline().strip())

    while n != 0:
        p = int(stdin.readline().strip())
        print( power_sum(n, 1 , p))
        n = int(stdin.readline().strip())

def power_sum(n, m, p):
    tmp =  pow(m , p)
    if( tmp == n):return 1
    if(tmp > n ): return 0
    return power_sum(n, m+1,p ) + power_sum(n-tmp, m+1, p)

main()