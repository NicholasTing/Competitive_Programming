import math
T = int(input())

while T != 0:

    n,k = map(int,input().split())

    count = 0
    index = 0

    x = math.floor(k / (n-1))
    if ((x +k) % n == 0):
        ans = x + k -1
    else:
        ans = x + k
    
    print(ans)

    T -= 1