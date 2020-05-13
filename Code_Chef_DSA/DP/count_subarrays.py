T = int(input())

while T != 0:

    T -= 1
    n = int(input())
    num = list(map(int,input().split()))

    dp = [0] * n
    for i in range(n):
        if num[i] >= num[i-1]:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = 1
    
    print(sum(dp))
        

