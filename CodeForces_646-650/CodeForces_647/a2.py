t = int(input())

while t != 0:
    a,b = map(int,input().split())
    t -= 1
    if a == b:
        print(0)
    elif a < b:
        shifts = [3,2,1]
        ans = 0
        count = 0
        while a <= b and count < 3:
            if a << shifts[count] <= b:
                a = a << shifts[count]
                ans += 1
            else:
                count += 1
        
        if a == b:
            print(ans)
        else:

            print(-1)

    elif a > b:
        shifts = [3,2,1]
        ans = 0
        count = 0
        while a >= b and count < 3:
            if a >> shifts[count] >= b:
                test_a = str(bin(a))
                if '1' in test_a[-shifts[count]:]:

                    count += 1 
                    continue
                a = a >> shifts[count]
                ans += 1
            else:
                count += 1
        
        if a == b:
            print(ans)
        else:
            print(-1)