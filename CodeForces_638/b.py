T = int(input())

while T != 0:
    n, k = map(int,input().split())
    numbers = list(map(int,input().split()))
    final_ans = []
    current_total = 0
    current_k = 0
    N = len(numbers)
    curr_index = 0
    for num in numbers:
        if current_k < k:
            final_ans.append(num)
            current_total += 1
            current_k += 1
            
            
        

        current_index += 1

        

    print('final ans')
    print(final_ans)

    T -= 1