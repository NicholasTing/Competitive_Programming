T = int(input())

while T != 0:
    n = int(input())
    num = list(map(int,input().split()))
    ans = sorted(num)
    lowest = 999999
    for i in range(n-1):
        if ans[i+1] - ans[i] < lowest:
            lowest = ans[i+1] - ans[i]
    
    print(lowest)

    T -= 1