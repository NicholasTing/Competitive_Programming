T = int(input())

while T != 0:

    N, K = map(int, input().split())
    num = list(map(int,input().split()))
    #sorted numbers
    snum = sorted(num)

    solution = False
    j = 0
    first_iter = True
    fa = []

    diff = [i for i in range(len(num)) if num[i] != snum[i]]
    # print(diff)
    if len(diff) > (K/3):
        print('-1')
    
    else:
        iters = 0
        while K != 0:
            wa = []
            wai = []
            count = 0
            if num == snum:
                solution = True
                break
            
            # print(num)
            # if not first_iter:
            #     diff = [i for i in range(len(num)) if num[i] != snum[i]]
            #     j = diff[0]

            for i in range(j,N):
                
                if num[i] != snum[i]:
                    wa.append(num[i])
                    wai.append(i)
                    count += 1
                
                if count == 3:
                    break
            
            swaperoo = False
            if count < 3:
                for i in range(j+iters,N):
                    if num[i] == snum[i] and num[i] not in wa:
                        wa.append(num[i])
                        wai.append(i)
                        count += 1
                        swaperoo = True
                    if count ==3:
                        break

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
            # print('num here')

            if j == N:
                first_iter = False
                j = 0
            
            if a != []:
                fa.append(a)
                # print(a)
                # print(num)
                K -= 1
            
            j += 1
            if num[j:N] == snum[j:N]:
                j = 0
                first_iter = False
            
            if swaperoo:
                j = 0
                iters +=1 
                if iters == N:
                    iters = 0
            
            print(num)
            
        
        if solution:
            #answer
            print(len(fa))
            for i in fa:
                print(' '.join([str(e) for e in i]))
            pass
        else:
            print('-1')
    
    T -= 1