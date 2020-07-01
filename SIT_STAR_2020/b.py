a,b,c,d,e = map(int,input().split())

total_comps = 0

while c != 0 and d != 0 and e != 0:
    if c - 1 >= 0 and d - 1 >= 0 and e - 1 >= 0:
        c -= 1
        d -= 1
        e -= 1
        total_comps += 1

while a != 0 and b != 0 and d != 0 and e != 0:
    if a - 1 >= 0 and b - 1 >= 0 and d - 1 >= 0 and e-1 >= 0:
        a -= 1
        b -= 1
        d -= 1
        e -= 1
        total_comps += 1

print(total_comps)

