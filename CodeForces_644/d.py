import math
T = int(input())

def Prime(n):
    if n & 1 == 0:
        return 2
    d= 3
    while d * d <= n:
        if n % d == 0:
            return d
        d= d + 2
    return 0

while T != 0:
    T -= 1
    n,k = map(int,input().split())
    ans = 0

    # print('n and k')
    # print(n)

    # print(k)
    if k >= n:
        ans = 1
        print(ans)
        continue

    else:

        answer = Prime(n)
        if answer == 0:
            print(n)

        else:
            if answer < k:
                i = answer
                while i <= k:
                    if (n % i == 0) and int(n/i) <= k:
                        ans = i
                        break

                    # if (n % i == 0) and int(n/i) * i == k:
                    #     print('here')
                    #     ans = int(n/i)
                    #     break
                    
                    # elif n % i == 0 and i < k:
                    #     ans = int(n/i)
                    i += 1
                
                if ans == 0:
                    # print('here')
                    for i in range(2,k):
                        if n % i == 0:
                            ans = n / i
                            
                print(int(ans))
    
                    
                # print(i)
                # print(answer)

            else:
                print(n)
  

