T = int(input())

while T != 0:
    N = int(input())
    nums = list(map(int,input().split()))
    print(nums)

    ai = 0
    bi = len(nums)
    ansi = [ai,bi]
    turn = 0
    ans = [0, 0]

    c = 0
    while ai != bi:
        
        print('a2')
        print(turn)
        print(ansi)
        while ans[turn%2] < ans[(turn+1)%2]:
            
            if ansi[turn%2] == ansi[(turn+1)%2]:
                break
            index = ansi[turn%2]
            if turn % 2 == 0:
                add = nums[index] + ans[turn%2]
                ans[turn%2] = add
                ansi[turn%2] = 1 + ansi[turn%2]
            else:
                add = nums[index] + ans[turn%2]
                ans[turn%2] = add
                ansi[turn%2] = ansi[turn%2] - 1

        
        [ai,bi] = ansi
        turn += 1
        print(ansi)
        # print(ai)
        # print(bi)
        # print(ansi)
        # c+= 1
        # if c == 10:
        #     break

    print(ans)


    T -= 1