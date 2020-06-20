from collections import defaultdict
t = int(input())
while t != 0:
    t -= 1
    n = int(input())
    ppl = list(map(int,input().split()))
    coins = defaultdict(int)
    if n == 1:
        if ppl[0] == 5:
            print('YES')
        else:
            print('NO')
        
    else:
        if ppl[0] == 5:
            coins[5] = 1