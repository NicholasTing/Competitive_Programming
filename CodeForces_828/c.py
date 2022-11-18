t = int(input())

while t != 0: 
    [n, c] = list(input().split(" "))
    letters = input()

    total = len(letters)

    check = letters + letters

    highest = 0
    current = 0
    for i in check:
        if i == c:
            current += 1
        
        elif i == 'g':
            highest = max(current, highest)
            current = 0
        
        else:
            if current != 0:
                current += 1
            

    print(highest)

    t -= 1