import math
t = int(input())
while t != 0:
    a,b = map(int,input().split())
    total = 0
    multiplier = 9
    initial_b = b
    initial_a = a

    while multiplier != 1:
        while a - 3 * (10 ** multiplier) >= 1 and b - 3 * (10 ** multiplier) >= 1:
            total += 2 * (10 ** multiplier)
            a -= 3 * (10 ** multiplier)
            b -= 3 * (10 ** multiplier)
        
        multiplier -= 1

    if initial_a < initial_b:
        while a - 3 >= 1 and b - 3 >= 1:
            total += 2
            a -= 3
            b -= 3
        print('b less than a')
        multiplier = 9
        while multiplier != -1:
            while a - 2 * (10 ** multiplier) >= 0 and b - 1 * (10 ** multiplier) >= 0:
                total += 1 * (10 ** multiplier)
                a -= 2 * (10 ** multiplier)
                b -= 1 * (10 ** multiplier)
            
            # print(a)
            # print(b)
            multiplier -= 1
        
        print(a)
        print(b)
        
        multiplier = 9
        while multiplier != 1:
            while a - 1 * (10 ** multiplier) >= 0 and b - 2 * (10 ** multiplier) >= 0:
                total += 1 * (10 ** multiplier)
                a -= 1 * (10 ** multiplier)
                b -= 2 * (10 ** multiplier)
            
            multiplier -= 1
    
    else:
        while a - 3 >= 1 and b - 3 >= 1:
            total += 2
            a -= 3
            b -= 3
        multiplier = 9
        while multiplier != 1:
            while a - 1 * (10 ** multiplier) >= 0 and b - 2 * (10 ** multiplier) >= 0:
                total += 1 * (10 ** multiplier)
                a -= 1 * (10 ** multiplier)
                b -= 2 * (10 ** multiplier)
            
            multiplier -= 1
        
        print(a)
        print(b)
        multiplier = 9
        while multiplier != -1:
            while a - 2 * (10 ** multiplier) >= 0 and b - 1 * (10 ** multiplier) >= 0:
                total += 1 * (10 ** multiplier)
                a -= 2 * (10 ** multiplier)
                b -= 1 * (10 ** multiplier)
            
            # print(a)
            # print(b)
            

            multiplier -= 1
        


                
    print(total)
    t -= 1