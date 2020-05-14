import math
T = int(input())

while T != 0:
    T -= 1
    n = int(input())

    if n == 1:
        print('0')
    
    else:
    
        ans = int((n-1)/2)
        print(ans)
        squared_in_view = (n-1)
        count = 1
        fa = 0
        while ans != 0:
            fa += squared_in_view ** 2 * count
            count += 1
            squared_in_view -= 1
            # print(i)
            ans -= 1
        
        print(fa)
        
        # print(tots*8 + (n-3) * (ans-1) * 4)
            

