t = int(input())

while t != 0:
    n = int(input())
    nums = list(map(int,input().split(" ")))
    word = input()

    found = False
    assign_words = {}
    for i in range(len(word)):
        if nums[i] not in assign_words:
            assign_words[nums[i]] = [word[i]]
        else:
            assign_words[nums[i]].extend(word[i])

    for key, val in assign_words.items():
        if len(set(val)) != 1:
            found = True
            break
    
    if not found:  
        print("YES")
    else:
        print("NO")           

    t-= 1