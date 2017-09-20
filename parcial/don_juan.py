

from sys import stdin
def main():
    T = int(stdin.readline().strip())
    for i in range(T):
        n = int(stdin.readline().strip())
        print(  2 * fib2(n))

def fib(n):
    d = [0 for i in range(n + 1)]
    d[0] = 1
    d[1] = 1
    for i in range(2 , n+1):
        d[i] = d[i-1] + d[i-2]
    #print("fib", d[n])
    return  d[n]

def fib2(n):
    if(n == 0): return 1
    elif n == 1: return 1
    else:
        return fib2(n-1) + fib2(n-2)



main()