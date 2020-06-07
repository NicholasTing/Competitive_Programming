# https://leetcode.com/contest/biweekly-contest-25/problems/max-difference-you-can-get-from-changing-an-integer/
class Solution:
    def maxDiff(self, num: int) -> int:
        
        
        nl = [int(x) for x in str(num)]
        a = []
        a_is_max = False
        highest = nl[0]
        curr_max = False

        if highest == 9:
            #find_second_highest
            count = 0
            while count < len(nl):
                if highest != 9:
    
                    break
                highest = nl[count]

                count += 1
            
            if count == len(nl):
                curr_max = True
                
        if curr_max:
            a = nl
        
        else:
            for i in nl:
                if i == highest:
                    a.append(9)
                else:
                    a.append(i)
        

        highest = nl[0]
        first_highest = True
        b_is_min = False
        b = []
        if highest == 1:
            first_highest = False
            count = 0
            while count < len(nl):
                if highest != 1 and highest != 0:
                    break
                highest = nl[count]
                count += 1
            
            if count == len(nl):
                b_is_min = True
        
        if b_is_min:
            b = nl
          
        else:
            for i in nl:
                if i == highest:
                    if first_highest:
                        b.append(1)
                    else:
                        b.append(0)
            
                else:
                    b.append(i)

        a_s = [str(i) for i in a]
        a_st = "".join(a_s)
        a_i = int(a_st)
        b_s = [str(i) for i in b]
        b_st = "".join(b_s)
        b_i = int(b_st)
        # print(a)
        # print(b)

        return a_i - b_i
      
        
        
        
        