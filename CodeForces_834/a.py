t = int(input())

while t != 0:
    ques = input()    
    
    found = False
    test_str = "Yes" * 100
    if ques in test_str:
        print("YES")
    else:
        print("NO")


    t-= 1

    
