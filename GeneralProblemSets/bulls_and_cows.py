# https://codeforces.com/problemsets/acmsguru/problem/99999/486

first = input()
second = input()

bulls = 0
cows = 0

count = 0
for digit in first:
    if second[count] == digit:
        bulls += 1
    
    count += 1

count = 0
for digit in second:
    if digit in first and digit != first[count]:
        cows += 1
    
    count += 1

print("%d %d" % (bulls,cows))