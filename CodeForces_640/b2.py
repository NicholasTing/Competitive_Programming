T = int(input())

while T != 0:
    n,k = map(int,input().split())
    even = False
    odd = False
    type_even = n / k
    if n % k == 0:
        ans = n/k
        print("YES")
        fa = [int(ans)]* k
        print(' '.join([str(e) for e in fa]))
    
    elif n < k:
        print("NO")
    
    else:
        if k == 2:
            print("NO")
        
        elif (n%2) == 0 and (k%2) == 1:
            
            if ((n-2)/(k-1)) % 2 == 0:
                ans = 2 * (k-1)
                print("YES")
                fa = [2] * (k-1)
                fa.append(n-ans)
                print(' '.join([str(e) for e in fa]))

            elif (n/(k+1) % 2) == (((n/(k+1)) * 2) % 2):
                ans = n/(k+1)
                fa = [int(ans)] * (k-2)
                fa.append(int(ans)*2)
                print("YES")
                print(' '.join([str(e) for e in fa]))
            
            else:
                print("NO")

        
        elif (n%2) == 1 and (k%2) == 0:
           
            print("NO")

            
        elif (n%2) ==1 and (k%2) == 1:
            ans = 1 * (k-1)
            fa = [1] * (k-1)
            if (n-ans) % 2 == 0:
                print("NO")
            else:
                fa.append(n-ans)
                print("YES")
                print(' '.join([str(e) for e in fa]))

    T -= 1