# LeetCode No.1822 Sign of the Product of an Array

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        result = 1
        
        for n in nums:
            if n < 0:
                result *= -1
            elif n == 0:
                result *= 0
                break
        
        return result