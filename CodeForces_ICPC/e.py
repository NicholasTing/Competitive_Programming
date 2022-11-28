import math

t = int(input())

while t!=0:
    n,a,b = map(int, input().split(" "))
    total = 0

    numSilverPerQuest = a

    if a > b:
        numSilverPerQuest = math.floor(a/b) * a + (a % b)
    
    min_num_quests = math.ceil(n/numSilverPerQuest)
    print(min_num_quests)
    t-= 1