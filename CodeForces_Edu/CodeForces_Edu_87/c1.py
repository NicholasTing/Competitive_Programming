import math
T = int(input())

while T !=0:
    n = int(input())
    
    if n == 2:
        print('1')
    
    else:
        side = math.tan(math.pi/(2*n))
        print(1/side)
    
    T -= 1