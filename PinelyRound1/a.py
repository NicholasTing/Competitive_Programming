t=int(input())

from itertools import permutations

while t != 0:
    [n,a,b] = list(map(int, input().split(" ")))

    if (n == a and n == b):
        print("Yes")

    elif (n - (a+b) > 1):
        print("Yes")
    
    else:
        print("No")
        
    t-=1