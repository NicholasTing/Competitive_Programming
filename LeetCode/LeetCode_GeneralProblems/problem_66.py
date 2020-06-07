# https://leetcode.com/problems/plus-one/
# Problem 66

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit = ''
        digits = map(str, digits)
        answer = digit.join(digits)
        
        answer_int = int(answer)
        answer_int += 1
        return list(str(answer_int))