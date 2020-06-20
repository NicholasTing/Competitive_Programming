t = int(input())
while t != 0:
    t -= 1
    friends = input()

    if len(friends) == 1:
        print(0)
    else:
        first_friend = friends[0]
        total = 0
        pair_found = False
        for i in friends[1:]:
            if i != first_friend and not pair_found:
                pair_found = True
                total += 1
            else:
                pair_found = False
            
            first_friend = i
    
        print(total)

