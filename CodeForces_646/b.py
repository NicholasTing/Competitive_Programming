T = int(input())

while T != 0:
    nums = input()
    T -= 1
    ans = 0
    fa = ''

    if len(nums) <= 3:
        if '010' == nums:
            print(1)
        elif '101' == nums:
            print(1)
        else:
            print(0)

    else:
        # Make all zeroes or make all ones
        # This one, we make all zeroes
        zeroes = 0
        if nums[0] == '1':
            zeroes += 1
        for i in nums[1:-1]:
            if i == '1':
                zeroes += 1

        ones = 0
        # This one, make all ones
        for i in nums[1:-1]:
            if i == '0':
                ones += 1
    
        if zeroes > ones:
            print(ones)
        else:
            print(zeroes)
