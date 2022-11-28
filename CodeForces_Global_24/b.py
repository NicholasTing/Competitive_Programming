from math import gcd
t = int(input())

while t != 0:
    n = int(input())
    nums = list(map(int, input().split(" ")))
    
    answer = 0
    for i in nums:
        answer = gcd(answer, i)

    final_ans = int(nums[n-1]/answer)

    print(final_ans)
    t-=1