T = int(input())

while T != 0:

    N, K = map(int, input().split())
    num = list(map(int,input().split()))
    #sorted numbers
    snum = sorted(num)
    fa = []
    solution_found = False
    while K != 0:
        if num == snum:
            solution_found = True
            break

        wa = []
        wai = []

        first_err = False

        count = 0
        for i in range(N):

            if num[i] != snum[i]:
                first_err = True
                wa.append(num[i])
                wai.append(i)
                count += 1
        
        if first_err:
            num1 = wa[0]
            numi1 = wai[0]
            rp = snum.index(num1)
            rpe = snum[rp]


            

        

            
        

        a = []
        if count == 3:
            num1 = wa[0]
            num2 = wa[1] 
            num3 = wa[2]

            numi1 = wai[0]
            numi2 = wai[1]
            numi3 = wai[2]

            num.remove(num1)
            num.insert(numi2,num1)
            num.remove(num2)
            num.insert(numi3,num2)
            num.remove(num3)
            num.insert(numi1,num3)
            a.append(numi1+1)
            a.append(numi2+1)
            a.append(numi3+1)
        
        if count == 2:
            num1 = wa[0]
            num2 = wa[1]

            
        
        elif count == 2 and not first_iter:
            num1 = wa[0]
            num2 = wa[1]
            
            numi1 = wai[0]
            numi2 = wai[1]

            num.remove(num1)
            num.insert(numi2, num1)
            num.remove(num2)
            num.insert(numi1,num2)  
            a.append(num1+1,num2+1)

        fa.append(a)
        K -= 1

    
    if num == snum:
        print(len(fa))
        for i in fa:
            print(' '.join([str(e) for e in i]))
    else:
        print("-1")

    T -= 1