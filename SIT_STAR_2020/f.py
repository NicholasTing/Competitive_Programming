n, k = map(int,input().split())


nums = list(map(int,input().split()))
count = 0
lowest_v = [False for i in range(k+1)] 

lowest = 0
seen = []
fa = [0 for i in range(n)]
numbers_to_add = [i for i in range(1,k+1)]

# for i in nums:
#     if i not in seen:
#         seen.append(i)
#         lowest_v[i-1] = False
#         fa.append(i)
#     else:
#         while lowest_v[lowest] != True:
#             lowest += 1
    
#         lowest_v[lowest] = False
#         seen.append(lowest+1)
#         fa.append(lowest+1)

temp = set(nums)
# print(numbers_to_add)
for i in temp:
    lowest_v[nums.index(i)] = True
    # print(nums.index(i))
    fa[nums.index(i)] = i
    numbers_to_add.remove(i)

# print(numbers_to_add)

# print(lowest_v)
# print(fa)

lowest = 1
i = 0
while i < len(fa):
    if not lowest_v[i]:
        to_add = numbers_to_add.pop(0)
        fa[i] = to_add
    
    i += 1

# print(fa)

print(' '.join([str(e) for e in fa]))



