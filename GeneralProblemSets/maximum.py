# https://codeforces.com/problemset/problem/1326/B

N = int(input())

numbers = list(map(int,input().split()))

a = []
x = [0]
highest = numbers[0]
for i in range(N):
    a.append(x[i]+numbers[i])
    if x[i]+numbers[i] > highest:
        highest = numbers[i]+x[i]

    x.append(highest)

print(' '.join([str(e) for e in a]))
