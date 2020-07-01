n = int(input())
i = 1

def sum_of_digits(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r

soln = False
ans = []
if n == 1:
    print(1)
else:
    while i <= 1000000000:
        ans = sum_of_digits(i+1) + sum_of_digits(i+2)
        if ans == n:
            soln = True
            ans = [i+1,i+2]
            break
        i += 2

if not soln:
    print(-1)
else:
    print(' '.join([str(e) for e in ans]))