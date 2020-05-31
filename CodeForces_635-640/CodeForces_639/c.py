t = int(input())

while t != 0:
    n = int(input())
    if n == 1:
        num = int(input())
        print("YES")
        
    else:
        num = list(map(int,input().split()))
        seen = []
        duplicate = False
        for i in range(n):
            if num[i] == 0:
                num[i] = n

            if (num[i] + i % n) not in seen:
                seen.append(num[i] + i % n)
            else:
                duplicate = True
                seen.append(num[i] + i % n)
                # break
        
        if duplicate:
            print("NO")
        else:
            print("YES")

    t -= 1