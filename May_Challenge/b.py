from collections import defaultdict
T = int(input())

while T != 0:

    N,Q = map(int,input().split())

    s = input()
    answer = defaultdict(int)
    for letter in s:
        answer[letter] += 1    

    while Q != 0:
        count = 0
        C = int(input())
        out = 0

        for letter,count in answer.items():
            if count > C:
                out += count - C

        print(out)
        Q -= 1
    
    T -= 1