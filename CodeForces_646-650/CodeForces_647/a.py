t = int(input())

while t != 0:
    a,b = map(int,input().split())
    t -= 1
    if a == b:
        print(0)
    elif a > b:
        if a % b != 0:
            print(-1)
            continue
        
        elif a % b == 0 and b == 1:
            print(-1)
            continue
        ops = [8,4,2]
        count = 0
        ans = 0
        same = 0
        while a >= b and count < 3:
            if a / ops[count] >= b and a % ops[count] == 0:
                a = a / ops[count]
                ans += 1
            else:
                count += 1
        
        if a == b:
            print(ans)
        else:
            print(-1)
    
    elif a < b:
        temp = a
        a = b
        b = temp
        if a % b != 0:
            print(-1)
            continue
        
        elif a % b == 0 and b == 1:
            print(-1)
            continue

        ops = [8,4,2]
        count = 0
        ans = 0
        same = 0
        while a >= b and count < 3:
            if a / ops[count] >= b and a % ops[count] == 0:
                a = a / ops[count]
                ans += 1
            else:
                count += 1

        if a == b:
            print(ans)
        else:
            print(-1)
    
    
    else:
        print('decided later')


