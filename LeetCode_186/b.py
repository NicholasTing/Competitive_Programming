# class Solution:
#     def best_score(self, cardPoints, k, direction,numbers_seen):
        
#         # print(numbers_seen)
#         if k in numbers_seen:
#             if direction == 'L':
#                 if numbers_seen[k] > cardPoints[0]:
#                     return numbers_seen[k]
#                 else:
#                     numbers_seen[k] = cardPoints[0]
#                     return numbers_seen[k]
        
#             else:
#                 if numbers_seen[k] > cardPoints[-1]:
#                     return numbers_seen[k]
#                 else:
#                     numbers_seen[k] = cardPoints[-1]
#                     return numbers_seen[k]
                
#         if k == 1 and direction == 'L':
#             if k in numbers_seen:
#                 if numbers_seen[k] < cardPoints[0]:
#                     numbers_seen[k] = cardPoints[0]
#                     return cardPoints[0]
#                 else:
#                     return numbers_seen[k]
            
#             numbers_seen[k] = cardPoints[0]
#             return cardPoints[0]
                
#         if k == 1 and direction == 'R':
#             if k in numbers_seen:
#                 if numbers_seen[k] < cardPoints[-1]:
#                     numbers_seen[k] = cardPoints[-1]
#                     return cardPoints[-1]
#                 else:
#                     return numbers_seen[k]
            
#             numbers_seen[k] = cardPoints[-1]
#             return cardPoints[-1]
        
#         if direction == 'L':
#             best_current_score = cardPoints[0]
#             best_right = self.best_score(cardPoints[1:],k-1, 'R',numbers_seen) + best_current_score
#             best_left = self.best_score(cardPoints[1:],k-1,'L',numbers_seen) + best_current_score

#         else:
#             best_current_score = cardPoints[-1]
#             best_right = self.best_score(cardPoints[:-1],k-1,'R',numbers_seen) + best_current_score 
#             best_left = self.best_score(cardPoints[:-1],k-1,'L',numbers_seen) + best_current_score
        
#         print(numbers_seen)
#         if best_right > best_left:
#             if k in numbers_seen and numbers_seen[k] < best_right:
#                 return best_right
            
#             numbers_seen[k] = best_right 
#             return numbers_seen[k]
    
#         else:
#             print(numbers_seen)
#             if k in numbers_seen and numbers_seen[k] < best_left:
            
#                 return best_left
            
#             numbers_seen[k] = best_left
#             return numbers_seen[k]
        
        
#     def maxScore(self, cardPoints: List[int], k: int) -> int:
        
#         if len(cardPoints) == k:
#             return sum(cardPoints)
    
#         result = all(elem == cardPoints[0] for elem in cardPoints)
#         if result:
#             answer = 0
#             count = 0
#             while k != 0:
#                 answer += cardPoints[count]
#                 count += 1
#                 k-= 1
            
#             return answer
    
        
#         left = self.best_score(cardPoints,k+1,'L',{})
#         right = self.best_score(cardPoints,k+1,'R',{})
#         if left > right:
#             return left
#         else:
#             return right
        
    
import functools
class Solution:     
    
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        if len(cardPoints) == k:
            return sum(cardPoints)

        # Try sliding window approach
        best_score = sum(cardPoints[-k:])
        print(best_score) 
        curr_best = best_score

        front_index = 0
        while k - front_index > 0:
            curr_best = curr_best + cardPoints[front_index] - (cardPoints[-k+front_index])
            
            # print(-k+front_index)
            # print(curr_best)
            # print(curr_best)

            if curr_best > best_score:
                best_score = curr_best
            
            
            front_index += 1
        
        final = sum(cardPoints[:front_index])
        if final > best_score:
            return final
        
        return best_score
        