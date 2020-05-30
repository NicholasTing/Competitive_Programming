T = int(input())
while T != 0:
    n,m,k = map(int,input().split())
    if m == 0:
        print(0)
    else:
        per_hand = n/k
        highest = int(n/k) - m
        total_joker = m
        total_joker_others = highest - m
        print(total_joker_others)
        
    T -= 1