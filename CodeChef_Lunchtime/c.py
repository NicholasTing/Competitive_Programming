T = int(input())

while T != 0:
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    total_together = 0
    count = 0
    alen = 0 
    blen = 0 

    while count != len(a):
        alen += a[count]
        blen += b[count]

        if alen == blen and a[count] == b[count]:
            total_together += a[count]
        
        count += 1
        

    print(total_together)

    T -= 1