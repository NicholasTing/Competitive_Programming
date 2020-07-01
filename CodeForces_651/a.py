t = int(input())

def isPrime(n) : 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True

    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True
  

while t != 0:
    n = int(input())
    if n == 2 or n == 3:
        print(1)    
    else:
        while isPrime(n):
            n -= 1
        print(int(n/2))
    t -= 1
