t = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

def find_equal(a,b,current_best_ind):
    ans = 0
    (best, best_index) = current_best_ind
    now_best = 0
    for i in range(len(a)):
        if i > best_index and ans < best:
            return (0,0)
        if a[i] == b[i]:
            ans += 1
            now_best = i
    return (ans,now_best)

curr_best, curr_best_index = find_equal(a[0:t],b,(0,0))
best = 0 
a_temp = a + a + [a[0]]
count = 0
bstr = ''.join([str(e) for e in b])
astr = ''.join([str(a) for a in a_temp])
if bstr not in astr:
    print(0)

else:
    for i in range(1,len(a_temp)-t):
        curr_best, curr_best_index = find_equal(a_temp[i:i+t],b,(best,curr_best_index))
        if curr_best > best:
            best = curr_best
        
        count += 1

    print(best)

