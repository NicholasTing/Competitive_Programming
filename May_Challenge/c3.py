T = int(input())

while T != 0:

    N, K = map(int, input().split())
    num = list(map(int,input().split()))
    #sorted numbers
    snum = sorted(num)

    # first parse to find all wrong indexes
    answer_out = []

    while K != 0 and num != snum:
        wa = {}
        index = []
        srcdest = []
        for i in range(N):
            if num[i] != snum[i]:
                index.append(i)
                srcdest.append((i, snum.index(num[i]),num[i]))

        zipdex = {index[i]: srcdest[i] for i in range(len(index))} 
        swaps = []
        for i,j in zip(index,srcdest):
            (src,dest,numb) = j
            if len(swaps) == 3:
                break
            if dest in index:
                swaps.append(i)
                zipsrc, zipdest, numb = zipdex[dest]
        
        string_out = []
        # print(zipdex)
        print(num)
        count = 0
        for src in swaps:
            if count == 3:
                break
            (src,dest,num1)  = zipdex[src]
            # (src2,dest2,num2) = zipdex[dest]
            # (src3,dest3,num3) = zipdex[dest2]
            temp1 = num1
            # temp2 = num2
            # temp3 = num3
            # num.remove(num1)
            num.insert(dest,temp1)
            num.remove(num1)
            # num.remove(num2)
            # num.insert(dest2,temp2)
            # num.remove(num3)
            # num.insert(dest3,temp3)
            string_out.append(src+1)
            # string_out.append(src2+1)
            # string_out.append(src3+1)
            # break'
            count += 1
            print(num)

        # print('string out')
        print(string_out)
        print(num)

        K -= 1
    

    T -= 1