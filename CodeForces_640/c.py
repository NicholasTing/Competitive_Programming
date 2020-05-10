T = int(input())

while T != 0:

    n,k = map(int,input().split())

    count = 0
    index = 0

    i = 1
    
    test = [i for i in range(1000000000) if i % n != 0]
    print(test[k])


    

    T -= 1