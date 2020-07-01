n,k = map(int,input().split())

if k == 2:
    print(-1)
else:
    alt = True
    ans = []
    low = 1
    high = n
    low_t = True
    while len(ans) != n:
        if low_t:
            low_t = False
            ans.append(low)
            low += 1
        else:
            low_t = True
            ans.append(high)
            high -= 1
            
    print(' '.join([str(e) for e in ans]))
