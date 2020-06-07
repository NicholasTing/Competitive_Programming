T = int(input())

while T != 0:
    N = int(input())
    nums = list(map(int,input().split()))
    if len(nums) == 1:
        print('1')
    
    elif sorted(nums,reverse=True) == nums:
        print('1')

    else:
        
        index = 1
        count = 1
        while (count) < len(nums):

            sc = count
            while sc < len(nums):
                sc = sc + 1
        
    T -= 1