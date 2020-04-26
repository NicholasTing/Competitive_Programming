class Solution:
    def maxScore(self, s: str) -> int:
        
        best_score = 0
        for i in range(1,len(s)):
            left = s[:i]
            right = s[i:]

            if left.count('0') + right.count('1') > best_score:
                best_score =  left.count('0') + right.count('1')
        
        return best_score