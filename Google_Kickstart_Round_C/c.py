from collections import defaultdict
T = int(input())
fa = []

perfect_num = [i**2 for i in range(0,101)]

# print(perfect_num)
seen = defaultdict(list)
while T != 0:
    n = int(input())
    nums = list(map(int,input().split()))

    # print(answer)
    count = 0
    ca = []
    answer = 0
    while count < n:
        seen = defaultdict(list)
        count2 = count
        ca = []
        while count2 <= n:
            count3 = count
            count3_array = []
            while count3 < count2:
                arr = nums[count3]
                count3_array.append(nums[count3])
                count3 += 1

            if count3_array not in seen[count]:
                seen[count].append(count3_array)
                ca.append(count3_array)
        
            count2 += 1
        
        
        count += 1
        for i in ca:
            if sum(i) in perfect_num and i != []:
                # print(i)
                answer += 1
            
        # print(ca)
    # print(answer)
    
    fa.append(answer)


    T -= 1

# print(fa)

count = 1
for i in fa:
    print('Case #' + str(count) + ': ' + str(i))
    count += 1