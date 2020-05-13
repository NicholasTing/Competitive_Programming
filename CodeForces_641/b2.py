T = int(input())

while T != 0:
    n = int(input())
    nums = list(map(int,input().split()))
    nums.insert(0,0)

    index = [1] * (n+1)
  
    for i in range(1,n):
        j = i * 2
        while j <= n:
            if nums[i] < nums[j]:
                index[j] = max(index[j], index[i]+1)
            j += i

    print(max(index))

    T -= 1