# https://codeforces.com/problemset/problem/1343/B

test_cases = int(input())
answer = []
answer_numbers = []

while test_cases != 0:
    number = input()
    number = int(number)

    even_half = []
    odd_half = []
    each_half = number / 2
    if number % 4 != 0:
        answer.append("NO")
        continue

    while each_half != 0:
        even_half.append(each_half * 2)
        each_half -= 1
    
    target_sum = int(sum(even_half))
    print(target_sum)
    count = 1
    while target_sum != 0:

        if target_sum - count == 0:
            target_sum = target_sum - count
            odd_half.append(count)
        
        elif target_sum - count > 0:
            target_sum = target_sum - count
            
        else:
            count = count * 2 + 1
    
    answer = even_half + odd_half
    answer_numbers.append(answer)

    test_cases -= 1
    number = int(input())

print(odd_half)