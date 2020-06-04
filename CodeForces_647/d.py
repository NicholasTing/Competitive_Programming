from collections import defaultdict
import heapq

blog, reference = map(int,input().split())

n = reference
adjlist = defaultdict(list)
while n != 0:
    a,b = map(int,input().split())
    adjlist[a].append(a)
    adjlist[b].append(a)
    n -= 1

desired = list(map(int,input().split()))
desired_enum = [(j+len(adjlist[i+1])/100,(i+1,adjlist[i+1])) for i,j in list(enumerate(desired))]
# print(desired_enum)
if len(set(desired)) == 1:
    print(-1)

else:

    q = []
    for i in desired_enum:
        heapq.heappush(q,i)

    ans = []
    seen = []
    while q:
        next_item = heapq.heappop(q)
        (x,y) = next_item
        number, nodes = y
        if number not in seen:
            seen.append(number)
            ans.append(number)
        for i in nodes:
            if i not in seen:
                val = (desired[i-1]+len(adjlist[i])/100, (i, adjlist[i]))
                heapq.heappush(q, val)
            elif i in adjlist[i]:
                adjlist[i].remove(i)
        # heapq.heappush(q,i)

    fa = ' '.join([str(e) for e in ans])
    print(fa)