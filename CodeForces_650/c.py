t = int(input())
while t != 0:
    t -= 1
    n,k = map(int,input().split())
    nums = list(map(int,input()))

    i = 0
    total_added = 0
    first_seen = False
    count = 1
    index = 0
    first_number = True
    while i < len(nums):
        if nums[i] == 0 and first_number:
            if 1 not in nums[i:i+k]:
                i = i+k-1
                total_added += 1
            
            if i + k > len(nums):
                break
            first_number = False
        else:
            first_number = False

        if nums[i] == 1:
            count = 0

        elif count == k * 2 + 1:
            total_added += 1    
            count = 0

        elif i == len(nums) - 1 and count > k:

            total_added += 1
    
        i += 1
        count += 1
    
    print(total_added)