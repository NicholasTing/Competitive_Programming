T = int(input())

fa = []

while T != 0:
    n,k = map(int,input().split())
    nums = list(map(int,input().split()))

    # print(nums)
    
    total = 0
    count = 0 
    temp_k = k
   
    total = 0
    temp_k = k
    for i in nums:

        if i == temp_k:
            temp_k -= 1
        
        elif i == k:
            temp_k = k -1

        else:
            temp_k = k

        if i == 1 and temp_k == 0:
            total += 1
            temp_k = k 

    fa.append(total)

    T -= 1

count = 1
for i in fa:
    print('Case #' + str(count) + ': ' + str(i))
    count += 1