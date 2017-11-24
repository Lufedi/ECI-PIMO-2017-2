



INF = 9999999999999999999
V = 9
def minDistance(dist, sptSet):

    min = INF
    min_index = -1
    for v in range(V):
        if sptSet[v] == False and dist[v]<= min:
            min = dist[v]
            min_index  =  v
    return  min_index

def dijkstra(graph, src):

    dist = [INF]* V
    sptSet = [False] * V
    dist[src] = 0
    for count in range(V-1):
        u =  minDistance(dist, sptSet)
        sptSet[u] = True
        for v in range(V):
            if not sptSet[v] and graph[u][v] != 0 and dist[u] != INF:
                if dist [u] + graph[u][v]  < dist[v]: #condicion de relajacion
                    dist[v] = dist [u] + graph[u][v]


    return  dist


graph = []
for i in range(V):
    graph.append( [0] * V)

edges  = ["0 1 4",
          "1 2 8",
          "2 3 7",
          "3 4 9",
          "4 5 10",
          "3 5 14",
          "2 5 4",
          "2 8 2",
          "8 6 6",
          "6 5 2",
          "7 6 1",
          "7 8 7",
          "7 1 11",
          "0 7 8"]

for edge in edges:
    data = edge.split(" ")
    graph[int(data[0])][int(data[1])] = int(data[2])
    graph[int(data[1])][int(data[0])] = int(data[2])
print(dijkstra(graph, 0))