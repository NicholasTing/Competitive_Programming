import math
from functools import reduce 
        
nums = input()

# Taking input as list, remove the '[ ]' brackets
nums = nums[1:-1].split(',')

# Convert into the elements of list to nums
nums = [int(x) for x in nums]

n = len(nums)
index = 0 
answer = []
# Dictionary will store values that we have seen before so we do not need
# to calculate everything again
product_of_everything = {}

for i in range(n):
    
    # If seen, add it into final array
    if nums[i] in product_of_everything:
        answer.append(product_of_everything[nums[i]])

    # If not, calculate the answer
    else:

        temp_array = []
        index = 0
        for number in nums:
            if index != i:
                temp_array.append(number)
            index += 1

        product = reduce((lambda x, y: x * y), temp_array) 
        product_of_everything[nums[i]] = product
        answer.append(product)
            
print(answer)