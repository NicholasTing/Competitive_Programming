T = int(input())

while T != 0:
    x, y = map(int, input().split())
    a, b = map(int,input().split())

    num = 0
    count = 1000000000

    while (x >0 or x <0) or (y< 0 or y > 0):

        count = 1000000000
        init = 0

        if x > 0 and x != 1:
            while count >= x  and count / 10 > 0:
                if count <= 0:
                    count = 1
                    break
                count = count / 10

        elif x < 0 and x != -1:
            while -count < x and count / 10 > 0:
                count = count / 10
                if count == 0:
                    count = 1
                    break
        
        elif y > 0 and y != 1:
            while count > y and count / 10 > 0:
                if count <= 0:
                    count = 1
                    break
                count = count / 10
        
        elif y < 0 and y != -1:
            while -count < y and count / 10 > 0:
                count = count / 10  
                if count == 0:
                    count = 1
                    break

        print('c')
        print(count)
        if count < 0:
            count = 1
        elif x < 10 and y < 10:
            count = 1
        
        count = int(count)
        
        print(x)
        print(y)

            
        if x-(1*count)== 0 and y- (1*count) == 0:
            x -= 1 * count
            y -= 1 * count
            num += b * count
        
        elif x+(1*count)== 0 and y +(1*count) == 0:
            x += 1 * count
            y += 1 * count
            num += b * count
        
        elif x+(1*count) ==0 and y-(1*count) == 0:
            x += 1*count
            y -= 1 *count
            num+= 2 * a * count
        
        elif x-(1*count) ==0 and y+(1*count) == 0:
            x -= 1*count
            y += 1 *count
            num+= 2 * a * count
        
        elif x - (1*count) == 0 and y == 0:
            x -= 1 * count
            num += a * count    
        
        elif x == 0 and y - (1*count) == 0:
            y -= 1 * count
            num += a * count
        
        elif x + (1*count) == 0 and y == 0:
            x += 1 * count
            num += a * count
        
        elif x == 0 and y + (1*count) == 0:
            y += 1 * count
            num += a * count
        
        elif x >= 1*count:
            x -= 1 * count
            num += a * count

        elif y >= 1*count:
            y -= 1 * count
            num += a * count
        
        elif x <= -1*count:
            x += 1 * count
            num += a * count
        
        elif y <= -1*count:
            y += 1 * count
            num += a * count

       
    print(int(num))
    T -= 1
        
