from functools import lru_cache
from fractions import gcd
from functools import reduce

def find_gcd(list):
    x = reduce(gcd, list)
    return x

n = int(input())
nums = list(map(int,input().split()))

def tgcd(N,nums):

    l = min(nums)
    print(list(reversed(range(l+1))))
    for i in reversed(range(2,l+1)):
        cd = True
        for j in range(N):
            if nums[j] % i != 0:
                cd = False
                break
        if cd:
            return i
    
    return 1

def ez_gcd(x, y): 
    while(y): 
        x, y = y, x % y 
    return x 

def find_lcm(n1, n2): 
    if(n1>n2): 
        num = n1 
        d2 = n2 
    else: 
        num = n2 
        d2 = n1 
    rem = num % d2 
    while(rem != 0): 
        num = d2 
        d2 = rem 
        rem = num % d2 
    gcd = d2 
    lcm = int(int(n1 * n2)/int(gcd)) 
    return lcm 

# Python program to find the L.C.M. of two input number

# This function computes GCD 
def compute_gcd(x, y):

   while(y):
       x, y = y, x % y
   return x

# This function computes LCM
def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm


final_lcm = []
seen = []

repeated = 0

fa = []
def find_array():
    prev_seen = []
    total = 0
    calculated_before = []
    for i in range(len(nums)-1): 
        if i in calculated_before:
            continue
        calculated_before.append(i)
        for j in range(i+1,len(nums)):
            
            num1 = nums[i] 
            num2 = nums[j] 
            lcm = compute_lcm(num1, num2) 
            if lcm in final_lcm:
                pass
            else:
                final_lcm.append(lcm)
    
find_array()
# print(final_lcm)
lcm = sorted(final_lcm)


# print(lcm)

# if len(lcm) == 1:
#     print(lcm[0])

# else:

    # n1=lcm[0] 
    # n2=lcm[1] 
    # gcd=ez_gcd(n1,n2) 

    # # print(lcm)
    # for i in range(2,len(lcm)): 
    #     gcd=ez_gcd(gcd,lcm[i])

    # ans = tgcd(len(final_lcm),final_lcm)
    # print(ans)
ans = find_gcd(final_lcm)
print(ans)

    # print(ans)