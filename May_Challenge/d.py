T = int(input())
while T != 0:

    # Case 1
    x,y,l,r = map(int,input().split())
    
    if x == 0 or y == 0:
        print('0')

    else:
        # numbers = [elem for elem in range(l,r)]
        current_bit = 1
        count = 0

        while current_bit <= l:
            current_bit = current_bit << count
            count += 1

        bits_to_multiply = []
        if l == 0 or r == 0:
            bits_to_multiply.append(0)
        if l == 1 or r == 1:
            bits_to_multiply.append(1)
        if l ==2 or r == 2:
            bits_to_multiply.append(2)
        if l ==3 or r==3:
            bits_to_multiply.append(3)

        while current_bit < r:
            current_bit = 1 << count
            bits_to_multiply.append(current_bit-1)
            count += 1
        
        highest = -1

        best_seen = 0

        for i in bits_to_multiply:
            curr = (x&i) * (y&i)
            
            if curr > highest:

                highest = curr
                best_seen = i
              
        best_multiplied = highest
   
        while True:
            bs = best_seen - 1
            best_multiplied = (x & bs) * (y & bs)
            
            if best_multiplied == highest:
                best_seen = best_seen - 1
            else:
                break

        print(best_seen)
            

        # while best == highest:
        # print(bits_to_multiply)
 
    T -= 1