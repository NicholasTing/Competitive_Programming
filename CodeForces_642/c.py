import math
T = int(input())

while T != 0:
    T -= 1
    n = int(input())

    if n == 1:
        print('0')
    
    else:
    
        ans = int((n-1)/2)
        init = 3
        ans = 0
        count = 1
        while init <= n:
            t = 2 * init + (2 * (init - 2))
            ans += t * count
            count += 1
            init += 2

        print(ans)
        
        # print(tots*8 + (n-3) * (ans-1) * 4)
            

