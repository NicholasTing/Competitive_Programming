T = int(input())

while T != 0:
    n = input()
    ans = []
    multiplier = 1
    while len(n) != 0:
        ans.append(int(n[-1]) * multiplier)
        multiplier *= 10
        n = n[:-1]
    
    fa = []
    for an in ans:
        if an != 0:
            fa.append(an)

    print(len(fa))
    print(' '.join([str(f) for f in fa]))


    T -= 1