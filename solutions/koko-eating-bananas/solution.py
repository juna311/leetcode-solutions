import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        k = left + (right - left) // 2
        while left < right:
            hours = 0
            for banana in piles:
                hours += math.ceil(banana / k)
            if h < hours:
                left = k + 1
                k = left + (right - left) // 2
            else: 
                right = k
                k = left + (right - left) // 2
        return right
        
            
                
