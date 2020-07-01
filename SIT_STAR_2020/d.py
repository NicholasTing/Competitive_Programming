n,k = map(int,input().split())
nums = list(map(int,input().split()))

def countPairs(a, n, k): 

    a.sort() 
    res = 0
    seen_index = []
    used_numbers = []
    seen = []
    fa = []
    for i in range(n):  
          
        # Keep incrementing result while 
        # subsequent elements are within limits. 
        j = i+1
        seen_index= []
        while (j < n and a[j] - a[i] <= k): 
            seen_index.append((i,j))
            res += 1
            j += 1
        
        for i,j in reversed(seen_index):
            if i not in used_numbers and j not in used_numbers:
                seen.append((i,j))
                used_numbers.append(i)
                used_numbers.append(j)
    
    print('final')
    print(seen)

    return res 
  

A = nums
diff = k

ans = countPairs(nums,n,k)
print(ans)
