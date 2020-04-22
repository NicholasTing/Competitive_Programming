# https://codeforces.com/contest/877/problem/A

check = input()
d = "Danil"
o = "Olya"
s = "Slava"
a = "Ann"
n = "Nikita"

friends = [d,o,s,a,n]

repeat_friends = False
no_friends = 0
unique_friends = 0
check = check.lower()

for friend in friends:

    friend = friend.lower()
    test = check.split(friend)
    if test[0] == check:
        no_friends += 1

    if len(test) == 2:
        unique_friends += 1
    
    if len(test) > 3:
        repeat_friends = True
        break
    
if repeat_friends:
    print("NO")

elif no_friends == 5:
    print("NO") 

elif unique_friends == 1:
    print("YES")

else:
    print("NO")