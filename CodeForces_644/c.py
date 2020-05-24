T = int(input())

while T != 0:
    n = int(input())
    T -= 1
    nums = list(map(int,(input().split())))
    nums = sorted(nums)

    number_even = [i for i in nums if i % 2 == 0]
    number_odd = [i for i in nums if i % 2 == 1]
    if len(number_even) % 2 == 0 and len(number_odd) % 2 == 0:
        print("YES")
        continue
    
    if len(nums) == 2:
        if nums[0] % 2 == nums[1] % 2:
            print("YES")
            continue
        if nums[0] == nums[1] + 1 or nums[0] == nums[1] - 1:
            print("YES")
            continue

        else:
            print("NO")
            continue
    
    soln =  False
    times_gone_through = 0
    while len(number_even) % 2 != 0 and len(number_odd) != 0 and times_gone_through != 5:

        times_gone_through += 1

        if len(number_even) > len(number_odd):
            for i in number_even:
                if i - 1 in number_odd:
                    number_odd.remove(i-1)
                    number_even.append(i-1)

                elif i + 1 in number_odd:
                    number_odd.remove(i+1)
                    number_even.append(i+1)
                
                if len(number_even) % 2 == 0 and len(number_odd) % 2 == 0:
                    print("YES")
                    soln = True
                    break
        
        else:
            for i in number_odd:
                if i - 1 in number_even:
                    number_even.remove(i-1)
                    number_odd.append(i-1)

                elif i + 1 in number_even:
                    number_even.remove(i+1)
                    number_odd.append(i+1)
                
                if len(number_even) % 2 == 0 and len(number_odd) % 2 == 0:
                    print("YES")
                    soln = True
                    break


    if soln:
        continue

    print("NO")


        
