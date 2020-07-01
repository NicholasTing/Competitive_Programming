n = int(input())

i = 0
count = 0
while i != n:
    count += 1
    if count % 3 == 0 or count % 7 == 0:
        i +=1


print(count)
    