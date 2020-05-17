T = int(input())

while T != 0:
    a, k = map(int,input().split())
    k -= 1
    while k != 0:
        k -= 1
        init = a
        a = str(a)  
        a = [int(e) for e in str(a)]

        if min(a) == 0:
            a = init + min(a) * max(a)
            break
        a = init + min(a) * max(a)
        # print(a)
    
    print(a)
    
    T -= 1