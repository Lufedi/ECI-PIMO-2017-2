

INF  = 100000000000000000000


def floydWarshall(graph):


    V = len(graph[0])
    dist = [[elem for elem in line] for line in graph]

    """ Add all vertices one by one to the set of intermediate
     vertices.
     ---> Before start of a iteration, we have shortest distances
     between all pairs of vertices such that the shortest
     distances consider only the vertices in set 
    {0, 1, 2, .. k-1} as intermediate vertices.
      ----> After the end of a iteration, vertex no. k is
     added to the set of intermediate vertices and the 
    set becomes {0, 1, 2, .. k}
    """
    for k in range(V):
        # pick all vertices as source one by one
        for i in range(V):
            # Pick all vertices as destination for the
            # above picked source
            for j in range(V):
                # If vertex k is on the shortest path from
                # i to j, then update the value of dist[i][j]
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

graph = [   [0, INF, INF, 1, 101],
            [INF, 0, 200, INF, INF],
            [INF, 200, 0, INF, 103],
            [INF, INF, 100, 0, INF],
            [INF, INF, 102, INF, 0]
        ]
floydWarshall(graph)
