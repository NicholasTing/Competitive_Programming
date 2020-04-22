# https://codeforces.com/contest/1343/problem/A

test_cases = int(input())

answers = []
while test_cases != 0:

    num = int(input())
    count = 1
    target = 0
    multiple = 2
    iterations = 0
    found = False
    
    while target != num:

        if target == num:
            found = True
            break

        target += count * (multiple ** iterations)

        if count > 2:
            break

        if target > num:
            target = 0
            iterations = 0
            count += 1
        
        if target == num:
            found = True
            break
            
    if found:
        answers.append(count)
    
    print(answers)
    
    
    test_cases -= 1

for answer in answers:
    print(answer)