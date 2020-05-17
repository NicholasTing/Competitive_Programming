import math
T = int(input())

while T != 0:
    a,b,c,d = map(int,input().split())

    if a <= b:
        print(b)
    
    elif d > c or d -c == 0:
        print('-1')
    
    else:
        minutes_slept = c - d
        time_needed = a - b
        time = math.ceil(time_needed / minutes_slept)
        # print('time')
        # print(time * c)
        answer = b + time * c
        print(answer)

    T -= 1