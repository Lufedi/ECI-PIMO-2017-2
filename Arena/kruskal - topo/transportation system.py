from sys import stdin
import math

class disjoin_set:

    def __init__(self):
        self.p = self
        self.rank = 0

def union(x, y):
    link(find_set(x), find_set(y))

def find_set(ds):
    if ds.p != ds:
        ds.p = find_set(ds.p)
    return ds.p

def link(x,y):
    if x.rank > y.rank:
        y.p = x
    else:
        x.p = y
        if x.rank == y.rank:
            y.rank = y.rank + 1

def main():
    cases = int(stdin.readline())
    for c in range(0, cases):
        data = stdin.readline().split()
        n = int(data[0])
        r = int(data[1])
        points = []
        for i in range(0, n):
            data = [int(x) for x in stdin.readline().split()]
            points.append((data[0], data[1]))
        edges = []
        sets = [disjoin_set() for x in range(0, n)]
        for i in range(0, n-1):
            for j in range(i+1, n):
                w = math.sqrt((points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2)
                edges.append((w,i,j))
        #Kruskal
        edges.sort()
        len_road = 0
        len_rail = 0
        num_reg = 1
        for e in edges:
            u = e[1]
            v = e[2]
            if find_set(sets[u]) != find_set(sets[v]):
                union(sets[u], sets[v])
                w = e[0]
                if w > r:
                    num_reg = num_reg + 1
                    len_rail = len_rail + w
                else:
                    len_road = len_road + w
        print('Case #%i: %i %.0f %.0f' % (c+1, num_reg, len_road, len_rail))

main()