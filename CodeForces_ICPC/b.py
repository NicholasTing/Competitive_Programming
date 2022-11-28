t = int(input())
while t!=0:
    n = int(input())
    a = input()

    if n == 1:
        print('YES')
    else:
        i = 0
        final_word = ""
        alt = True
        # Start with true
        while i < n:
            if alt:
                final_word += a[i]
                i += 1
            else:
                final_word += a[i]*2
                i += 2
            alt = not alt

        if final_word == a:
            print('YES')
        else:
            print('NO')

    t-= 1