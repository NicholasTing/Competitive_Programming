t = int(input())

while t != 0:
    [n, q] = list(map(int, input().split(" ")))
    nums = list(map(int, input().split(" "))) 

    final_ans = 0
    while q != 0:
        addEven = 0
        addOdd = 0 
        [type, num] = list(map(int,input().split(" ")))

        if (type == 0):
            addEven += num
        else:
            addOdd += num
        
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = nums[i] + addEven
            else:
                nums[i] = nums[i] + addOdd
        
        print(sum(nums))

        q -= 1

    t -= 1