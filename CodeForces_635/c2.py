from collections import defaultdict
import heapq
from queue import PriorityQueue

n, k = map(int, input().split())

NMAX = 200005

a = defaultdict(list)
father = defaultdict(int)
count_sons =  defaultdict(int)
level =  defaultdict(int)
count_marked =  defaultdict(int)

# priority queue
q = PriorityQueue()

def dfs(node, fth):
    father[node] = fth
    for son in edges[node]:
        if son == fth:
            continue
        count_sons[node] += 1
        level[son] = level[node] + 1
        dfs(son, node)
    
    if not count_sons[node]:       
        q.put((-level[node],node))
        # q.put((node,level[node],))
    
# initialise list
edges = defaultdict(list)

while n != 1:

    x,y = map(int, input().split())
    x -= 1 
    y -= 1

    edges[x].append(y)
    edges[y].append(x)

    n -= 1

dfs(0,-1)

ans = 0

while (k and not q.empty()):

    # print(list(q.queue))
    # print(father)
    if ans == 0 and once:
        break
    
    pair0, pair1 = q.get()
    # print(x)

    node_father = father[pair1]

    ans += pair0
    k -= 1
    count_marked[pair1] += 1

    if node_father != -1:
        count_sons[node_father] -= 1
        count_marked[node_father] += count_marked[pair1]

        if count_sons[node_father] == 0:
            # print('xd')
          
            q.put((-(level[node_father] - count_marked[node_father]), node_father))
            # print('h')
        
    once = True
print(abs(ans))