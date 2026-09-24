class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        number = 0
        streak = 0
        for n in nums:
            if n == 1:
                number += 1
                streak = max(streak, number)
            elif n == 0:
                number = 0
        return streak
            

                
        
        
        