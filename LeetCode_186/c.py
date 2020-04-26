class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        answer = []
        count = 0
        dp = [[0 for i in range(len(nums)+1000)] for j in range(len(nums)+1000)]
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if nums[i][j]:
                    dp[i][j] = 1
        
        # print(dp)
        
        R = len(nums)
        count_R = 0
        count_C = 0
        count_C_Start= 1
        total = 10000
        while dp[count_R][count_C] != 0 or total != 0:
    
            print(dp[count_R][count_C])
            while count_R >= 0 or dp[count_R][count_C] > 0:
                if dp[count_R][count_C] == 1:
                    # print(nums[count_R][count_C])
                    answer.append(nums[count_R][count_C])
                count_R -= 1
                count_C += 1
            
            if count + 1 == R:
                count_R = R - 1
                count_C = count_C_Start
                count_C_Start += 1
            else:
                count += 1
                count_R = count
                count_C = 0
                
            total -= 1
     
        return answer
            