T = int(input())

while T != 0:
    n = int(input())
    nums = list(map(int,input().split()))
    
    in_court = 1

    check = 0
    while True:
        if len(nums) == 0:
            break
        
        if len(nums) != 1:
            granny = nums[0]
            if granny < min(nums[1:]):
                print('impossible')
                break

        if len(nums) == 1:
            if granny <= in_court:
                in_court += 1
                break
        
        # print(nums)
        added = 0
        for i in sorted(nums):
            if i <= in_court or (i <= granny):
                added += 1
                in_court += 1
                nums.remove(i)
        
        if in_court <= granny:
            in_court -= added
            # print('failed')
            break
        
    
    print(in_court)

    T -= 1