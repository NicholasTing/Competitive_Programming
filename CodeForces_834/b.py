t = int(input())

while t != 0:
    [m,s] = list(map(int, input().split(" ")))
    b = list(map(int, input().split(" ")))

    target = sum(b) + s

    i = 1
    total = 0
    curr_sum = 0
    while total < target:
        if i not in b:
            curr_sum += i
        total += i
        i += 1
    
    if curr_sum == s:
        print("YES")
    else:
        print("NO")


    # if found:
    #     print("YES")
    # else:
    #     print("NO")

    t-=1
