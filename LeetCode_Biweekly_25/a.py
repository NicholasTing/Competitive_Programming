# https://leetcode.com/contest/biweekly-contest-25/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        answer = []
        most = max(candies)
        for candy in candies:
            if candy + extraCandies >= most:
                
                answer.append(True)
            else:
                answer.append(False)
            
        return answer