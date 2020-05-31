T = int(input())
while T != 0:
    n, k = map(int,input().split())
    s = input()
    index = 0
    fa = [[] for i in range(k)]    
    
    s = sorted(s)
    if k == 1:
        fa = s
        print(''.join(fa))
    else:
        
        s = sorted(s,reverse=True)
        s = s[:-1]
        for i in s:
            print(i)
        print(fa)
        print(s)
        
    
        # print(' '


    T -= 1