import math
T = int(input())

import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

while T != 0:
    x1,y1,x2,y2 = map(int,input().split())

    if x1 == x2:
        print(1)
    elif y1 == y2:
        print(1)
        
    else:
        ans = 0
        w = abs(y2-y1)
        h = abs(x2-x1)
        top = math.factorial(w+h)
        bot = math.factorial(w) * math.factorial(h)
     
        answer = top/bot

        number_of_duplicates = 0
        while x1 < x2 and y1 < y2:
            if x1 + 1 < x2 and y1 + 1 < y2:
                x1 += 1 
                y1 += 1
                number_of_duplicates += 1
            else:
                break
            
        answer = int(answer) - number_of_duplicates
      
        print(int(answer))

        # print(answer)
        
    T -= 1