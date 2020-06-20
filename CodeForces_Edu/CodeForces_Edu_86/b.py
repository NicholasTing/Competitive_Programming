T = int(input())

while T != 0:

    num = input()

    if num == len(num) * num[0] or len(num) == 2:
        same = True
    else:
        same = False
        
    if same:
        print(num)

    else:
        ans = ''
        for i in num:
            ans += '10'
        
        print(ans)

    T -= 1