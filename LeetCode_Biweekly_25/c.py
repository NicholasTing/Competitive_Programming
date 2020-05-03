# https://leetcode.com/contest/biweekly-contest-25/problems/check-if-a-string-can-break-another-string/
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        
        s1 = sorted(s1)
        # print(s1)
        s2 = sorted(s2)
        # print(s2)
                      
        if (s1 > s2):
            temp = s1
            s1 = s2
            s2 = temp

        breakable = False
        for i in range(len(s1)):
            # print('s2')
            # print(s2[i])
            # print('s1')
            # print(s1[i])
            # print(s2[i]<s1[i])
            # print('s2 ord')
            # print(ord(s2[i]))
            # print('s1 ord')
            # print(ord(s1[i]))
            if ord(s2[i]) < ord(s1[i]):
                breakable = True
                
        
        if not breakable:
            return True
        
        return False