t = int(input())

while t != 0:
    n = int(input())
    nums = list(map(int,input().split()))
    version = list(map(int,input().split()))
    t -= 1

    if 0 not in version or 1 not in version:
        if sorted(nums) == nums:
            print('Yes')
        else:
            print('No')
        continue
    
    elif sorted(nums) == nums:
            print('Yes')
    
    else:
        first_list = zip(nums,version)
        sorted_list = sorted(first_list)
        for i in sorted_list:
            (x,y) = i
            print(i)
        
        print(sorted(zip(nums,version)))
            
