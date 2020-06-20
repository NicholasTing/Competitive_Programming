
T = int(input())

while T != 0:

    x, y = map(int,input().split())
    a, b = map(int,input().split())

    total = 0 
    if x > y:
        temp = x
        x = y
        y = temp
    
    total += a * (y-x)
    if (2*a < b):
        total += 2 * x * a

    else:
        total += x * b
    
    print(total)

    T -= 1