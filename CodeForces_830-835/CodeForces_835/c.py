t=int(input())

# TLE for this solution
# Had to use cpp
while t != 0:
    n = int(input())
    nums = list(map(int, input().split(" ")))

    sorted_nums = sorted(nums)
    highest = sorted_nums[-1]
    secondHighest = sorted_nums[-2]

    final_list = ""
    for i in nums:
        if i == highest:
            final_list = final_list + (str(i-secondHighest)) + " "
        else:
            final_list = final_list + (str(i-highest)) + " "

    print(final_list)
    
    t-=1