from collections import defaultdict
import math

T = int(input())
while T != 0:
    N = int(input())
    nums = list(map(int,input().split()))
    nums = sorted(nums)

    total_groups = defaultdict(int)
    for i in nums:
        total_groups[i] += 1
    
    answer = 0
    kiv = []
    numbers_left = {}
    total_explorers_left = 0
    for key,val in total_groups.items():
        while val - key >= 0:
            total_groups[key] -= key
            answer += 1
            val = val - key
    
        if total_groups[key] != 0:
            kiv.append(key)
            numbers_left[key] = val
            total_explorers_left += val
    
    kiv = sorted(kiv)
    kiv_s = sorted(kiv)
    
    count = 0 
    solution_found = False
    len_kiv = len(kiv)
    explorer_gone = []
    # print('explorers left')
    # print(total_explorers_left)
    # print(kiv)
    # print(numbers_left)
    seen = 0
    for i in kiv:
        seen += numbers_left[i]
        if i - seen <= 0:
            seen = seen - i
            answer += 1    

    print(answer)

    T -= 1