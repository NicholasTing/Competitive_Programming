T = int(input())

while T != 0:
    N = int(input())
    nums = list(map(int,input().split()))
    ai = 0
    bi = len(nums) - 1
    a = 0
    b = 0
    turn = 0
    if N == 1:
        print('1 1000 0')

    else:
        prev_max = 0
        cl = True
        done = False
        while not done:
            curr_max = 0
            if turn % 2 == 0:
                
                while (a <= b or curr_max < prev_max):
                    if (abs(ai-bi) == 0):
                        done = True
                        break
                    curr_max += nums[ai]
                    a += nums[ai]
                    ai += 1
                cl = False

            else:
                while (b <= a or curr_max < prev_max):
                    if (abs(ai-bi) == 0):
                        done = True
                        break
                    curr_max += nums[bi]
                    b += nums[bi]
                    bi -= 1
                
                cl = True
                
            if not cl and bi == ai:
                a += nums[ai]
                break
            elif cl and bi == ai:
                b += nums[bi]
                break
 
            turn += 1
        
            prev_max = curr_max
            
        print('%d %d %d' % (turn,a,b))

    T -= 1