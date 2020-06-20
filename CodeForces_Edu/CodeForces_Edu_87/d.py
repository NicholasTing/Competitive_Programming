n ,q = map(int,input().split())

ms = list(map(int,input().split()))

qs = list(map(int,input().split()))

count = 0
neg_count = len(list(filter(lambda x: (x < 0), qs)))
neg_elems = list(filter(lambda x: (x < 0), qs))

if len(neg_elems) == len(ms):
    print('0')

else:
    while count < len(qs) and neg_count != 0:
        ms = sorted(ms)
        if neg_count == len(ms):
            ms = []
            break
    
        if qs[count] < 0:
            neg_count -= 1
            neg_elems.remove(qs[count])
            elem_to_pop = abs(qs[count]) - 1
            ms.pop(elem_to_pop)
        
        else:
            qs.append(qs[count])
        
    
        if neg_elems == []:
            break

        index = abs(neg_elems[0]) - 1
        # print(index)

        if index + 1 < len(ms) and ms[index] == ms[index+1]:

            print('index here')
            neg_elems.remove(neg_elems[0])
            ms.pop(index)
            neg_count -= 1
        
        # print(ms)
        # print('neg elems')
        # print(neg_elems)
        count += 1

    if ms == []:
        print('0')
    else:
        print(ms[0])
