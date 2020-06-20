t = int(input())
while t != 0:
    t -= 1
    n,k = map(int,input().split())
    nums = list(map(int,input().split()))
    ans = 0
    real = 0
    
    for i in nums:
        if i <= k:
            ans += i
        else:
            ans += k
        real += i
    
    print(real-ans)