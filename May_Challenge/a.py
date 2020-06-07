T = int(input())
while T != 0:
    num = int(input())
    ppl = list(map(int,input().split()))
    
    minimum = 20
    maximum = 1
    curr_max = curr_min = 0
    prev_infected = False

    for i in range(1,num):
        if prev_infected and ppl[i] - ppl[i-1] <= 2:
            curr_max += 1
            curr_min += 1
        
        elif not prev_infected and ppl[i]-ppl[i-1] <= 2:
            prev_infected = True
            curr_max = 2
            curr_min = 2
        
        elif ppl[i] - ppl[i-1] > 2:
            if curr_max > maximum:
                maximum = curr_max
            
            if curr_min < minimum:
                minimum = curr_min
            
            curr_min = 0
            curr_max = 0
            prev_infected = False
    
    if curr_max > maximum:
        maximum = curr_max
            
    if curr_min < minimum:
        minimum = curr_min

    if minimum == 0:
        minimum = 1
    
    print("%d %d" % (minimum,maximum))
    
    T -= 1