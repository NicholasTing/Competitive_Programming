T = int(input())

answer = []
while T != 0:
    num,a,b,c,d = map(int, input().split())

    lower_bound_a = num * (a - b)
    upper_bound_a = num * (a + b)

    lower_bound_c = c - d
    upper_bound_c = c + d

    possible = True
    if lower_bound_a > upper_bound_c:
        possible = False
    
    elif upper_bound_a < lower_bound_c:
        possible = False
    
    if possible:
        answer.append('Yes')
    else:
        answer.append('No')

    T -= 1

for ans in answer:
    print(ans)