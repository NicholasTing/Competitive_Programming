# https://codeforces.com/contest/877/problem/A

check = input()
d = "Danil"
o = "Olya"
s = "Slava"
a = "Ann"
n = "Nikita"

friends = [d,o,s,a,n]

unique_friends = 0

for friend in friends:

    test = check.count(friend)
    unique_friends += test
    # print(test)
    # if len(test) == 2:
    #     unique_friends += 1

if unique_friends == 1:
    print("YES")

else:
    print("NO")