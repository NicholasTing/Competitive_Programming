n = int(input())

i = 0

def sum_of_digits(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r

if n == 1:
    print(1)

elif n == 3:
    print('10 11')

else:
    if i < n:
        i = int(n/2)
        print(i)
        nines = int(str(int(i/9) * 300000))
        
    
    soln = False
    total = 0
    ans = []
    while total < n:
        total = sum_of_digits(nines+1) + sum_of_digits(nines+2)
        if total == n:
            ans = [nines+1,nines+2]
            soln = True
        nines += 2
        print(total)

    
    if soln:
        print(' '.join([str(e) for e in ans]))
    else:
        print(-1)

    

