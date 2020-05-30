T = int(input())
while T != 0:
    n,m,k = map(int,input().split())
    T -= 1
    if m == 0:
        print(0)
    
    elif n == m:
        print(0)
    
    elif m == 1:
        print(1)
    
    else:
        one_hand = int(n/k)
        joker = m
        if one_hand >= joker:
            print(joker)

        else:
            jokers_left = joker - one_hand
            if k == 2:
                 
                if jokers_left - one_hand >= 0:
                    print(0)
                else:
                    print(one_hand-1)
        

           

    
            
            

    
