T = int(input())

while T != 0:

    T -= 1
    g = int(input())
    goals = list(input())
    ans = [0,0]
    # print(ans)

    half = g / 2
    count = 0

    for i in goals:
        ans[count%2] += int(i)
        count += 1 
        
        if ans[count%2] - half > ans[(count+1)%2]:
            if count % 2 == 0:
                continue
            break
      
    
    print(count)