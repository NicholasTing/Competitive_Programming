t = int(input())
while t != 0:
    s = list(input())
    if len(s) == 2:
        print(''.join([str(e) for e in s]))
    else:
        first = s[0]
        i = 1
        while i <= len(s):
            first = first + s[i]
            i += 2
        
        print(first)

    t-= 1