t = int(input())

while t != 0:
    n,m = map(int,input().split())
    t -= 1
    total = n
    ans = []
    while total != 0:
        nums = list(map(int,input().split()))
        ans.append(nums)
        total -= 1
    
    tots = 0
    soln = False
    one_every_row = 0
    for i in ans:
        if 1 not in i:
            tots += 1
        elif 0 not in i:
            print('Vivek')
            soln = True
            break

        if 1 in i:
            one_every_row += 1

    if soln:
        continue
    
    if one_every_row == n:
        print('Vivek')
        continue

    if tots % 2 == 0:
        print('Vivek')
    else:
        print('Ashish')
