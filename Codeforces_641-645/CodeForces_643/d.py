N, S = map(int,(input().split()))

 
def printDistSum(arr, n): 
  
    Sum = sum(arr) 
       
    dp = [[False for i in range(Sum + 1)]  
                 for i in range(n + 1)] 
                   
    for i in range(n + 1):  
        dp[i][0] = True
    
    for i in range(1, n + 1): 
  
        dp[i][arr[i - 1]] = True
  
        for j in range(1, Sum + 1): 
            if (dp[i - 1][j] == True): 
                dp[i][j] = True
                dp[i][j + arr[i - 1]] = True
    
    answer = []
    for j in range(Sum + 1):  
        if (dp[n][j] == True): 
            # print(j, end = " ")
            answer.append(j)
    return answer

count = 1
fa = []

if S - N == 1:
    print('NO')

else:
    while count != N:
        fa.append(count)
        count += 1

    fa.append(S - sum(fa))
    answer = printDistSum(fa, len(fa))
    
    soln = False
    for i in range(S):
        if i in answer:
            print("NO")
            soln = True
            break
    
    if not soln:
        print("YES")
        print(' '.join([str(a) for a in fa]))
        print(i)
        soln = True

    
    