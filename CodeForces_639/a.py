T = int(input())

while T != 0:

    n, m = map(int,input().split())
    if n == 1:
        print("YES")
    elif n ==2 and m == 2:
        print("YES")
    elif m == 1:
        print("YES")
    else:
        print("NO")

    T -= 1