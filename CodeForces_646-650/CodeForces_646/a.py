T = int(input())

while T != 0:
    x,n = map(int,input().split())
    nums = list(map(int,input().split()))
    T -= 1
    if x == 1:
        if nums[0] % 2 == 1:
            print("Yes")
        
        else:
            print("No")
    
    elif x == n:
        if sum(nums) % 2 == 1:
            print('Yes')
        else:
            print('No')
    
   
    
    else:
        
        count = 0
        total_even = len([num for num in nums if num % 2 == 0])
        total_odd = len(nums) - total_even
        
        if total_odd == 0:
            print('No')
            continue
            
        else:
            
            if n - 1 - total_even <= 0:
                print('Yes')
                continue
            
            else:
                n = n - 1 - total_even
                total_odd -= 1
                total_even = 0
            
            if total_odd == 0:
                print('No')
                continue
            
            while total_odd > 0:
                total_odd -= 2
                if total_odd < 0:
                    print('No')
                    break
                if n - 2 == 0:
                    print('Yes')
                    break
                elif n - 2 < 0:
                    print('No')
                    break
                n -= 2
                    