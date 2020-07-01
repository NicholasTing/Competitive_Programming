from functools import lru_cache
t = int(input())
player_one = 'Ashishgup'
player_two = 'FastestFinger'

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

@lru_cache(maxsize=None)
def isWinning(n):
    if int(n) == 1:
        return False
    elif int(n) == 2:
        return True
    
    if n % 2 == 0:
        # print('greatest odd')
        greatest_odd_divisor = n/2
        # print(n/greatest_odd_divisor)
        isWinning(n/greatest_odd_divisor)
    else:
        isWinning(n-1)
    
    return True
    

while t != 0:
    t -= 1
    n = int(input())
    if isWinning(n):
        print(player_one)
    else:
        print(player_two)

    
    

