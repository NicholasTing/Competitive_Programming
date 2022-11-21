import math
t=int(input())

while t != 0:

    n = int(input())
    a = list(map(int, input().split(" ")))

    if n == 2:
        print(2)
    elif n == 1:
        print (1)
    else:
        total_diff = len(set(a))
        if total_diff == 2:
            print(int(n/2) + 1)
        else:
            print(n)
                        
    t-=1