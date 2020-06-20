T = int(input())

while T != 0:
    x,n = map(int,input().split())
    nums = list(map(int,input().split()))
    T -= 1
    if x == 1:
        if nums[0] % 2 == 1:
            print('Yes')
        
        else:
            print('No')
    
    elif x == n:
        if sum(nums) % 2 == 1:
            print('Yes')
        else:
            print('No')
    
    elif n > x:
        print('No')
    
    else:

        total_even = len([num for num in nums if num % 2 == 0])
        total_odd = len(nums) - total_even
        
        if total_odd == 0:
            print('No')
            continue
         
        else:

            if total_even != 0:

                odd_needed = n - 1 - total_even
                total_odd -= 1
                # print(odd_needed)
                if total_odd >= odd_needed:
                    print('Yes')
                else:
                    print('No')
            
            else:
                if n % 2 == 1:
                    print('Yes')
                else:
                    print('No')
            