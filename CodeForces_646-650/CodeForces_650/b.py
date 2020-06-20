import math
t = int(input())
while t != 0:
    n = int(input())

    nums = list(map(int,input().split()))
    i = 0

    count = 0
    wrong_elems_num = []
    wrong_elems_index = []

    while i < len(nums):
        if nums[i] % 2 != i % 2:
            wrong_elems_index.append(i%2)   
            wrong_elems_num.append(nums[i]%2)
            count += 1
        i += 1
    
    if sorted(wrong_elems_num) == sorted(wrong_elems_index):
        if count % 2 == 0:
            print(int(count/2))
        else:
            print(int(count/2)+1)
    else:
        print(-1)
    
    # print(count)

    t-= 1