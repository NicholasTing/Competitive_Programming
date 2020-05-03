# https://leetcode.com/contest/biweekly-contest-25/problems/number-of-ways-to-wear-different-hats-to-each-other/
from collections import defaultdict

class Solution:
    
    def __init__(self): 
        self.mask = 0
        self.hats = defaultdict(list)
        
    def findTotal(self, dp, mask, hat_num):
        if mask == self.mask:
            return 1
    
        if hat_num > 40:
            return 0
        
        if dp[mask][hat_num] != -1:
            return dp[mask][hat_num]
        
        total = self.findTotal(dp,mask,hat_num+1)
        
        if hat_num in self.hats:
            for people in self.hats[hat_num]:
                if mask & (1 << people):
                    continue
                
                total += self.findTotal(dp,mask | (1<< people), hat_num + 1)
                total = total % (10 ** 9 + 7)
            
        dp[mask][hat_num] = total
        return dp[mask][hat_num]
        
        return 0
        
    def numberWays(self, hats: List[List[int]]) -> int:
        N = len(hats)
        self.mask = (1 << N) -1
        count = 0
        for people in hats:
            for hat in people:
                self.hats[hat].append(count)
            count += 1
        
        dp = [[-1 for j in range(40 + 1)] for i in range(2 ** N)]
        ans = self.findTotal(dp,0,1)

        return ans
                
                
                
                
       