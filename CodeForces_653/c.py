t = int(input())

def find_best(ans):

    ltr = 0
    to_change = 0
    for i in ans:
        if i == '(':
            ltr += 1
        else:
            ltr -= 1
        
        if ltr < 0:
            to_change += 1
    
    rtl = 0
    to_change_rtl = 0
    for i in reversed(ans):
        if i == ')':
            rtl -= 1
        elif i == '(' and rtl < 0:
            rtl -= 1
        else:
            rtl += 1
        
        if rtl < 0:
            to_change_rtl += 1

    print('compare')
    print(to_change)
    print(to_change_rtl)
    if to_change > to_change_rtl:
        return to_change_rtl
        
    return to_change



while t != 0:
    t-= 1
    n = int(input())
    ans = input()
    fa = find_best(ans)
    print(fa)