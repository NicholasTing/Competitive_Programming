# https://codeforces.com/problemset/problem/1327/A

test_cases = int(input())

def recursive(odd, target, numbers_seen, numbers_used):
    if odd > target:
        return numbers_used
    
    elif odd == target:
        return numbers_used
    
    target += odd
    numbers_seen.append(odd)
    numbers_used.append(odd)

    odd = odd + 2

    return recursive(odd, target,numbers_seen, numbers_used)



while test_cases != 0:
    n , k = input().split()
    odd_seen = []
    odd_used = []
    curr_odd = 0
    count = 1

    answer = recursive(curr_odd, int(n), odd_seen, odd_used)
    print(answer)
    
    test_cases -= 1