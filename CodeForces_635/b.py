# Kana and Dragon Quest game
# https://codeforces.com/contest/1337/problem/B

import math
T = int(input())

while T != 0:
    
    # dragon hp, void, light
    h,v,l = map(int,input().split())
    total = 0

    target_hp = l * 10

    while h >= 0:

        if v == 0 and l == 0:
            break
        
        if h > target_hp:
            
            if v != 0:
                v -=1
                h = math.floor(h/2) + 10
                
            
            elif l != 0:
                l -= 1
                h -= 10
            
        elif h <= target_hp:
            l -= 1
            h -= 10
        
        elif v != 0:
            v -= 1
            h = math.floor(h/2) + 10


    # print(h)
    # print(l)
    # print(v)

    if h <= 0:
        print("YES")
    else:
        print("NO")
    


    T -= 1