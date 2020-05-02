
T = int(input())

while T != 0:

    x, y = map(int,input().split())
    a, b = map(int,input().split())
    real_a = a
    real_b = b

    ans = 0
    count = 1000000000
    while (x >0 or x <0) or (y< 0 or y > 0):

        if count > x:
            while count >= x:
                if count < 0:
                    count = 1
                    break
                count = count / 10
        
        elif -count < x:
            while -count <=x:
                if count < 0:
                    count = 1
                    break
                count = count / 10
        
        elif count > y:
            while count >= y:
                if count < 0:
                    count = 1
                    break
                count = count / 10
        
        elif -count < y:
            while -count <= y:
                if count < 0:
                    count = 1
                    break
                count = count / 10
        
        # x = x * count
        # print(x)
        # print(y)
        print(count)
        # y = y * count
        a = real_a * count
        b = real_b * count

        if x - count == 0 and y - count == 0:
            x -= count
            y -= count
            ans += b
        
        elif x + count == 0 and y + count == 0:
            x += count
            y += count
            ans += b
        
        elif x + count == 0 and y - count == 0:
            x += count
            y -= count
            ans += a
            ans += a
        
        elif x - count == 0 and y + count == 0:
            x -= count
            y += count
            ans += a
            ans += a
        
        elif x - count == 0:
            x -= count
            ans += a
        
        elif y - count == 0:
            y -= count
            ans += a
        
        elif x + count == 0:
            x += count
            ans += a
        
        elif y + count == 0:
            y += count
            ans += a
        
        elif x + count <= -1:
            x += count
            ans += a
        
        elif x - count >= 1:
            x -= count
            ans += a
        
        elif y + count <= -1:
            y += count
            ans += a
        
        elif y - count >= -1:
            y -= count
            ans += a
    
    print(int(ans))

    T -= 1