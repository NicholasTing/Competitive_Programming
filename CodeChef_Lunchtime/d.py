from collections import defaultdict
T = int(input())

def findMinDiff(arr, n): 
    arr = sorted(arr) 
    diff = 10**20
    for i in range(n-1): 
        if arr[i+1] - arr[i] < diff: 
            diff = arr[i+1] - arr[i] 
    return diff

travelled_Global = []
def dfs(adjlist, travelled, curr ,dest, prev):
    if curr == dest:
        return [(dest,a[dest])]
    
    if curr in travelled or (prev,curr) in travelled_Global:
        return [(curr,a[curr])]
    
    best = []
    travelled.append(curr)
    # where we can go
    for i in adjlist[curr]:
        dfsVal = dfs(adjlist,travelled,i,dest,curr)
        print(dfsVal)
        best.extend(dfsVal)
        travelled_Global.append((i,curr))
        # print(travelled)

    return best.extend([(curr,a[curr])])
    
while T != 0:
    adjlist = defaultdict(list)
    T -= 1
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    a.insert(0,0)
    # print(a)
    while n != 1:
        u,v = map(int,input().split())
        adjlist[u].append(v)
        adjlist[v].append(u)
        n -= 1
    
    while q != 0:
        src, des = map(int,input().split())
        tree = dfs(adjlist,[],des,src,-9)
        print(tree)
        # print(set(tree))
        b = [j for (i,j) in set(tree)]
        # a = [y for (x,y) in set(tree)]
        if len(b) == 1:
            b.append(a[des])
        min = float('-inf')

        ans = findMinDiff(b,len(b))
        print(ans)
 
        q -= 1
