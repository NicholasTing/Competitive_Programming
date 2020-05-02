
T = int(input())

while T != 0:

    x, y = map(int,input().split())
    a, b = map(int,input().split())

    ans = 0
    x_reduction = False
    y_reduction = False
    while (x >0 or x <0) or (y< 0 or y > 0):

        count = 1000000000
        if x < 10:
            x_reduction = True
        
        if y < 10:
            y_reduction = True

        while count > abs(x) and count > abs(y) and not x_reduction and not y_reduction:
            count = count / 10
        
        if not x_reduction:
            count = 1000000000
            while count >= abs(x):
                count = count/10
            
        if not y_reduction:
            count = 1000000000
            while count >= abs(y):
                count = count/10
        
        if x_reduction and y_reduction:
            count = 1
    
        # print(x)
        # print(y)
        print(x)
        print(y)
        if x - (1*count) == 0 and y - (1 * count) == 0:
            x -= 1 * count
            y -= 1 * count
            ans += b * count
        
        elif x + (1 * count) == 0 and y + (1*count) == 0:
            x += 1 * count
            y += 1 * count
            ans += b * count
        
        # elif x + (1 * count) == 0 and y - (1*count) == 0:
        #     x += 1 * count
        #     y += 1 * count
        #     ans += a * count
        #     ans += a * count
        
        # elif x - (1 * count) == 0 and y + (1*count) == 0:
        #     x += 1 * count
        #     y += 1 * count
        #     ans += a * count
        #     ans += a * count
        
        elif x - (1*count) >= 1 and y - (1 * count) >= 1:
            x -= 1 * count
            y -= 1 * count
            ans += b * count
        
        elif x + (1 * count) <= -1 and y + (1*count) <= -1:
            x += 1 * count
            y += 1 * count
            ans += b * count
        
        elif x + (1*count) <= 1:
            x += 1 * count
            ans += a * count
        
        elif y + (1*count) <= 1:
            y += 1 * count
            ans += a * count
        
        elif x - (1 * count) >= 1:
            x -= 1 * count
            ans += a * count
        
        elif y - (1*count) >= 1:
            y -= 1 * count
            ans += a * count

    print(int(ans))
    T -= 1