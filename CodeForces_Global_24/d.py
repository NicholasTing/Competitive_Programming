import  math
import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom  # or / in Python 2

def nPr(n, r):
    return math.factorial(n)/(math.factorial((n-r)))

def range_prod(lo,hi):
    if lo+1 < hi:
        mid = (hi+lo)//2
        return range_prod(lo,mid) * range_prod(mid+1,hi)
    if lo == hi:
        return lo
    return lo*hi

def treefactorial(n):
    if n < 2:
        return 1
    return range_prod(1,n)

n, p = map(int,input().split(" "))

view = n
if n % 2 ==0:
    total = 0
    print(treefactorial(view) % p - (view-1) ** 2 + 1)


else:
    total = 0
    for i in range(1,view):
        total += treefactorial(i) % p

    print(total % p * 5)