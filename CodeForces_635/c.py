from collections import defaultdict
import heapq
from queue import PriorityQueue

n, k = map(int, input().split())

NMAX = 200005
INF = 1000000000
MOD = 1000000007

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
        # q.put(level[node], (level[node],node))
        # q.put((level[node],node), level[node])
        # q.put((-level[node],node), level[node])
        q.put((-level[node],-node))
        
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

# heap = list(q.queue)
# heapq._heapify_max(heap)
print(father)
while (k != 0 and not q.empty()):

# while k != 0 and heap != []:

    # print(father)
    # print(heap)
    # pair = heapq._heappop_max(heap)
    print(list(q.queue))    
    
    pair = q.get()
    # print(list(q.queue))
    # print(pair)
    print(pair)
    print(father)
    node_father = (father[-pair[1]])
    ans += (-pair[0])
    k -= 1
    count_marked[-pair[1]] += 1

    if node_father != -1:
        count_sons[node_father] -= 1
        count_marked[node_father] += count_marked[-pair[1]]

        if count_sons[node_father] == 0:
            # q.put((-(level[node_father] - count_marked[node_father]), node_father))
            q.put((-(level[node_father]-count_marked[node_father]),-node_father))
        
print(ans)