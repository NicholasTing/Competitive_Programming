from collections import defaultdict
T = int(input())

while T != 0:
    n,x = map(int,input().split())
    adjlist = defaultdict(list)
    leaf = []
    parents = []
    while n != 1:
        u,v = map(int,input().split())
        if v not in parents:
            parents.append(v)
        
        if u not in leaf:
            leaf.append(u)

        adjlist[v].extend([u])
        n -= 1
    
    print(adjlist)
    print(parents)
    print(leaf)

    T -= 1