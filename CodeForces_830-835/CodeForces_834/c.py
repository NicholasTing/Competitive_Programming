t=int(input())

while t!=0:
    [l,r,x] = list(map(int, input().split(" ")))
    [a,b] = list(map(int, input().split(" ")))

    found = False
    value = 0
    if a == b:
        value = 0
        print(value)
        t-=1
        continue

    # if both even
    found = False
    if b > 0:
        if a + x > r:
            found = True
            value = -1

    else:
        if a - x < l:
            found = True
            value = -1
    
    
    if not found:
        print("TBD")

    else:
        print(value)
    

    t-=1 