from functools import lru_cache
t = int(input())

@lru_cache(maxsize=None)
def recurse(m, n): 
  
    if(m == n): 
        return 0
  
    if(m > n): 
        return -0.5
  
    if(n % 2 == 1): 
        return 1 + recurse(m, n * 2) 

    else: 

        return 1 + recurse(m, n / 6) 

while t != 0:
    t -= 1
    n = int(input())
    seen = []
    i = 1
    fa = recurse(1,n)
    if int(fa) != fa:
        print(-1)
    else:
        print(fa)
        
