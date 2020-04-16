N = int(input())

def print_output(answer):
    count = 1
    for number in answer:
        print('Case #' + str(count) + ': ' + str(number))
        count += 1

answer = []
while N != 0:
    A, B  = map(int,input().split())
    numbers = sorted(list(map(int,input().split()))) 

    count = 0
    
    for number in numbers:
        if B - number >= 0:
            B = B - number
            count = count + 1
        
        else:
            break    

    answer.append(count)
        
    N = N - 1

print_output(answer)