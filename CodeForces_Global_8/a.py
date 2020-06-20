t = int(input())
while t != 0:
    a,b,n = map(int,input().split())
    t -= 1
    if a < b:
        lower = a
        higher = b
    else:
        lower = b
        higher = a
    
    i = higher
    count = 0
    n1 = lower
    n2 = higher
    while i <= n:

       i = n1 + n2
       n1 = n2
       n2 = i
       count += 1
    
    print(count)
