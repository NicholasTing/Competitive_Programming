t = int(input())

while t != 0:
    k = int(input())
    num = list(map(int,input().split()))
    
    fa = -1 
    for i in range(1,1025):
        ans = list(map(lambda j : j^i , num))
        # num2 = [i ^ j for j in num]
        # print(ans)
        if set(ans) == set(num):
        #     print('here')
            fa = i
            break
        # print(num2)
        # if num == num2:
        #     break
    print(fa)
    t -= 1