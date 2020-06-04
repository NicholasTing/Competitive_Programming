t = int(input())

while t != 0:
    n = int(input())
    ans = 0
    for i in bin(n)[2:]:
        if i == '1':
            ans += 1
    print((n*2)-ans)
    t -= 1
