import math
t = int(input())
while t != 0:
    t -= 1
    x,y,n = map(int,input().split())
    multiplier = math.floor(n/x)

    if (multiplier * x) + y > n:

        ans = ((multiplier -1) * x) + y
        print(ans)
    else:
        ans = (multiplier * x) + y
        print(ans)