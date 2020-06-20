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
    
    possible= [[True] * m for _ in range(n)]
    # print(possible)
    for i in range(n):
        for j in range(m):
            if ans[i][j] == 1:
                ans[i][j] = 0
                possible[i] = [False] * m
                for k in range(n):
                    possible[k][j] = False
    
    turn = 0
    allFalse = False
    while not allFalse:
        allFalse = True
        for i in range(n):
            for j in range(m):
                if possible[i][j] == True:
                    turn += 1
                    allFalse = False
                    ans[i][j] = 0
                    possible[i] = [False] * m
                    for k in range(n):
                        possible[k][j] = False
    
    if turn % 2 == 0:
        print('Vivek')
    else:
        print('Ashish')
                
                
