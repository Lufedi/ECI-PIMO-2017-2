
from sys import stdin

indegree = []
res = []
map = {}
our = "";
n = 0
G  = []

def backtrack(left):


    global res
    global indegree
    global n
    global G


    if(left == 0):
        print(res)
    for i in range(n):
        if indegree[i] == 0:

            indegree[i] = -1
            res[n-left] = unmap[i]
            for node in G[i]:
                indegree[node]-=1
            backtrack(left-1)
            for node in G[i]:
                indegree[node]+=1
            indegree[i] = 0;




def main():
    global res
    global indegree
    global map
    global unmap
    global n
    global G

    symbols = stdin.readline().strip().split(" ");
    comparators = stdin.readline().strip().split(" ");
    sorted(symbols)

    res = "";
    n = len(symbols)
    indegree = [0 for i in range(n)]
    unmap = [0 for i in range(n)]
    G = [[] for i in range(n)]
    for i in range(n):
        map[symbols[i]] = i
        unmap[i] = symbols[i]

    res = [0 for i in range(n)]

    for i in range(0,len(comparators),2):

        s = map[comparators[i]];
        t = map[comparators[i+1]]
        indegree[t] += 1
        G[s].append(t)


    backtrack(n)


main()