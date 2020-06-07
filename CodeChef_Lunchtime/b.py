T = int(input())

hrs = 24 * 5
while T != 0:
    a,b,c,d,e,p = map(int,input().split())
    T -= 1
    total = a + b + c + d + e
    ans = total * p
    if ans <= hrs:
        print("No")
    else:
        print("Yes")
