T = int(input())

while T != 0:

    N, K = map(int, input().split())
    numbers = list(map(int,input().split()))

    final_answer = sorted(numbers)
    final_append = []
    current_sorted_count = 0
    found_wrong = False

    while numbers != final_answer and K != 0:

        wrong_places = {}
        for i in range(current_sorted_count,N):
            if numbers[i] != final_answer[i]:
                found_wrong =True
                wrong_places[numbers[i]] = final_answer.index(numbers[i])
                current_sorted_count = i
                break
    
        if found_wrong:
            all_wrong_items = {}
            for val,index in wrong_places.items():
                find_next_place = final_answer[index]
                print(find_next_place)
                wrong_place = numbers[index]
                print(wrong_place)
        
        print(wrong_places)

        K -= 1
    
    if final_answer == numbers:
        print(len(final_append))
        for answer in final_append:
            print(answer)
    else:
        print('-1')

    T -= 1