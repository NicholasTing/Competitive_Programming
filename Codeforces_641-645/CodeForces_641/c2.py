from functools import lru_cache
from fractions import gcd
from functools import reduce

n = int(input())
nums = list(map(int,input().split()))

# This function computes GCD 
def compute_gcd(x, y):

   while(y):
       x, y = y, x % y
   return x

# This function computes LCM
def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm

gcd_array = [1] * n
gcd_array[n-1] = nums[n-1]
tn = n - 2
while tn >= 0:
    gcd_array[tn] = compute_gcd(gcd_array[tn+1],nums[tn])
    tn -= 1

ans_1 = [0] * n
# print(gcd_array)

for i in range(n-1):
    ans_1[i] = (nums[i] * gcd_array[i+1]) / gcd_array[i]
    
# print(ans_1)

final_ans = ans_1[0]
for i in range(2,n):
    final_ans = compute_gcd(final_ans, ans_1[i])

# for i in range(2,)
print(int(final_ans))
