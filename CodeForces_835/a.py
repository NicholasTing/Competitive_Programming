t=int(input())

while t != 0:
    nums = list(map(int, input().split(" ")))
    l = min(nums)
    r = max(nums)
    for i in nums:
        if i not in (l,r):
            print(i)
            
        
    t-=1