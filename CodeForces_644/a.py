T = int(input())


while T != 0:

    a,b = map(int,input().split())
    if a > b:
        if (b + b) >= a:
            ans = (b+b) ** 2
        else:
            ans = a ** 2
    
    elif b > a:
        if (a+a) >= b:
            ans =(a+a) ** 2
        else:
            ans = b ** 2

    else:
        ans = (a+b) ** 2

    print(ans)

    T -= 1