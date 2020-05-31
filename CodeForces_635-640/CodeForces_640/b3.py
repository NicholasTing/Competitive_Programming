T = int(input())

while T != 0:
    n,k = map(int,input().split())
   
    type_even = n / k

    n1 = n - (k-1)
    if n1 > 0 and n1 % 2== 1:
        print("YES")
        fa = [1] * (k-1)
        fa.append(n1)
        print(' '.join([str(e) for e in fa]))
        T -= 1
        continue
    
    n2 = n - 2 * (k-1)
    if n2 > 0 and n2 % 2 == 0:
        print("YES")
        fa = [2] * (k-1)
        fa.append(n2)
        print(' '.join([str(e) for e in fa]))
        T -= 1
        continue

    print("NO")
    T -= 1