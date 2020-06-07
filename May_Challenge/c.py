T = int(input())

while T != 0:

    N, K = map(int, input().split())
    numbers = list(map(int,input().split()))

    final_answer = sorted(numbers)

    wrong_places = {}
    final_append = []
    while numbers != final_answer and K != 0:

        index = 0
        changes = 0
        numbers_added = []
        fi_index = []
        wrong_places = {}
        for i in range(len(numbers)):
            if numbers[i] != final_answer[i]:
                wrong_places[index] = numbers[i]
                changes += 1
            if changes == 3:
                break

            index += 1
        
        for key,value in wrong_places.items():
            numbers_added.append(value)
            fi = final_answer.index(value)
            numbers.remove(value)
            numbers.insert(fi,value)
            fi_index.append(fi+1)
        
        # print(fi_index+)
        answers = ' '.join([str(e) for e in sorted(fi_index)])
        final_append.append(answers)

        K -= 1

    if final_answer == numbers:
        print(len(final_append))
        for answer in final_append:
            print(answer)

    else:
        print('-1')

    T -= 1