from sys import stdin
from math import *

def solve(P,Q,R,S,T,U):


    def fun(x):
        return P * exp(-1.0 * x) + Q * sin(x) + R * cos(x) +\
            S * tan(x) + T * x ** 2 + U
    if fun(1) * fun(0) > 0:
        return 'No solution'
    epi = 1E-9
    if fun(1.0) > fun(0.0):
        high, low = 1.0, 0.0
    else:
        high, low = 0.0, 1.0

    while abs(high - low) > epi:
        mid = (low + high) / 2.0
        f = fun(mid)
        if f > 0:
            high = mid
        elif f < 0:
            low = mid
    return '%.4f' % mid


line =  stdin.readline().strip()
while line != "":
    data= line.split()
    P = int(data[0])
    Q = int(data[1])
    R = int(data[2])
    S = int(data[3])
    T = int(data[4])
    U = int(data[5])
    print(solve(P,Q,R,S,T,U))
    line = stdin.readline().strip()
