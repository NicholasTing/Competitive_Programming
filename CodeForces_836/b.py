t = int(input())

while t != 0:
    n = int(input())
    if n == 1:
        print(69)
    else:
        if n % 2 == 0:
            if n == 2:
                print("1 3")
            else:
                ans = "1 3 " + ("2 " * (n-2))
                print(ans)

        else:
            ans = "7 " * n
            print(ans)
    t -= 1