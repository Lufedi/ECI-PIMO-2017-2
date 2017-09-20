
from sys import  stdin
def main(n):

    d  = [ 0  for i in range( n +1 )]
    d[0] = d[1] = d[2] = 1
    d[3] = 2
    for i in range(4, n+1):
        d[i] = d[i-1]+d[i-3]+d[i-4]
    print(d[n])


T =int(stdin.readline().strip())
for i in range(T):
    n = int(stdin.readline().strip())
    main(n)
