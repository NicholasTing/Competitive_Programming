T = int(input())

while T != 0:
    n, k = map(int,input().split())
    numbers = list(map(int,input().split()))
    # distinct numbers
    dn = set(numbers)
    dn_num = len(dn)
    if dn_num > k:
        print('-1')
        T -= 1
        continue
    
    else:
        fa  = []
        for i in dn:
            fa.append(i)
        
        while len(fa) < k:
            fa.append(1)
            
        fa = fa * n
        print(len(fa))
        print(' '.join([str(e) for e in fa]))

 
    T -= 1