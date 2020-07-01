t= int(input())
while t != 0:
    t-= 1
    n,k = map(int,input().split())
    nums = list(map(int,input().split()))
    w = list(map(int,input().split()))

    nums = sorted(nums)
    sum_of_happiness = 0
    w = sorted(w)
    for i in w:
        happiness = []
        maxi = True
        count = 0
        if i == 2:
            a = nums.pop()
            b = nums.pop()
            happiness.append(a)
            happiness.append(b)
        
        else:
            while i != 0:
                i -= 1
                if maxi:
                    a = nums.pop()
                    happiness.append(a)
                    maxi = False
                else:
                    a = nums.pop(0)
                    happiness.append(a)
            
            happiness = sorted(happiness)

        if len(happiness) == 1:
            sum_of_happiness += happiness[0] * 2
        else:
            sum_of_happiness += max(happiness)
            sum_of_happiness += min(happiness)
    
    print(sum_of_happiness)
            