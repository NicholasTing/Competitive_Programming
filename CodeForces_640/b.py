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
    
    else:
        if k == 2:
            print("NO")
        
        elif n % 2 == 0:
            even = n - 2
            fa = []
            if even % (k-1) == 0:
                ans = even / ( k-1)
                if ans % 2 == 0:      
                    an = [int(ans)] * (k-1)
                    an.append(2)
                    fa = an
                    print("YES")
                    print(' '.join([str(e) for e in fa]))
                else:
                    print("NO")
            
            else:
                if n % (k+1) == 0:
                    ans = n/(k+1)
                    an = [int(ans)] * (k-1)
                    an.append(int(ans)*2)
                    fa = an
                    print("YES")
                    print(' '.join([str(e) for e in fa]))

                
                else:
                    print("FALSE")
            
        
        elif n % 2 == 1:
            ans = 1 * (k-1)
            if (n-ans) % 2 == 1:
                print("YES")
                n = n-ans
                fa = [1] * (k-1)
                fa.append(n)
                print(' '.join([str(e) for e in fa]))


            else:
                print("NO")    
        

    T -= 1