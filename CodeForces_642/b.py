T = int(input())

while T != 0:
    T -= 1
    n,k = map(int,input().split())
    
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    a = sorted(a)
    b = sorted(b,reverse=True)
    count = 0
    # print(a)
    # print(b)
    ai_smaller = True
    if k == 0:
        print(sum(a))

    else:
        for i in range(len(a)):
            if a[i] < b[i]:
                a[i] = b[i]
                k -= 1
            if k == 0: 
                break
            elif a[i] > b[i]:
                break
    
        print(sum(a))
    