from collections import defaultdict

T = int(input())

while T != 0:
    a,b,q = map(int,input().split())

    answer = []
    while q != 0:
        l, r = map(int, input().split())
        seen = defaultdict(int)
        ans = 0
        for i in range(l,r+1):
            
            if i in seen:
                seen[i]

            if ((i % a) % b) != ((i %b) % a):
                ans += 1
                seen[i] = 1
            
        answer.append(ans)
        q -= 1
    
    final = ''
    print(' '.join([str(elem) for elem in answer]))


    T -= 1