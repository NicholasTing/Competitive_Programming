import math
T = int(input())

while T != 0:
    n,m = map(int,input().split())
    if n == 1:
        answer = math.ceil(m/2)
    
    elif m == 1:
        answer = math.ceil(n/2)
    
    else:
        answer = math.ceil((m*n)/2)

    print(answer)
    
    T -= 1