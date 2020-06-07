T = int(input())
while T != 0:
    n = int(input())
    nums = list(map(int,input().split()))
    print(sum(nums))
    T -= 1