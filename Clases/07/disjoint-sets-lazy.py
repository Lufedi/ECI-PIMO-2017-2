





parent = []
rank = []
def create_disjoint_set(n):
    global parent
    global rank
    parent = [i for i in range(n+1)]
    rank = [0 for i in range(n + 1)]



def find_path_compression(x):
    global  parent
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def find(x):
    global parent
    if parent[x] != x:
        return  find(parent[x])
    else:
        return x

def union(x, y):
    global parent
    x_root = find(x)
    y_root = find(y)
    parent[x_root] = y_root

def union_ranking(x, y):
    global parent
    global rank
    x_root = find(x)
    y_root = find(y)
    if x_root == y_root:
        return

    if rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[x_root] = y_root
        if rank[x_root] == rank[y_root]:
            rank[y_root] = rank[y_root] + 1

#element : 1 2 3 4 5 6 7 8
#parent  : 3 3 3 3 5 5 7 8

#element : 1 2 3 4 5 6 7 8
#parent  : 1 2 3 4 5 6 7 8

#parent: [1,1,2,3,4]
#parent: [1,1,1,1,1]

create_disjoint_set(8)
print("created ", parent)
union(1, 2)
union(2, 3)
print("created ", parent)



create_disjoint_set(8)
print("created ", parent)
union_ranking(1, 2)
union_ranking(2, 3)
print("created ", parent)
