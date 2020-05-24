T = int(input())

while T != 0:
    num = int(input())
    arr = []
    while num != 0:
        arap = list(map(int,input()))
        arr.append(arap)
        num -= 1
    
    ans = True
    for i in range(len(arr)-1):

        for j in range(len(arr[i])-1):

            if arr[i][j] == 1:
                
                if arr[i+1][j] != 1 and arr[i][j+1] != 1:
                    ans = False
                    break

    if ans:
        print("YES")
    else:
        print("NO")

    T -= 1