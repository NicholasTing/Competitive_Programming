t = int(input())
while t != 0:
    t-= 1
    n = int(input())
    num = input()
    i = 0
    final = ''
    if n == 1:
        print(n)
        continue
    elif n == 2:
        if num == '11':
            print('11')
        elif num == '10':
            print('0')
        elif num == '01':
            print('01')
        else:
            print('00')
    else:
        fs = ''
        seen_0 = False
        seen_zero = False
        num = reversed(num)
        for i in range(n):
            if num[i] == '0' and num[i+1] == '0':
                fs = num[i] + fs
            elif num[i] == '1' and num[i+1] == '0':
                fs = num[i+1]
            el

