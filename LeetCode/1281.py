# LeetCode No.1281 Subtract the Product and Sum of Digits of an Integer

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nums = list(str(n))
        prod = 1
        plus = 0
        
        for num in nums:
            prod *= int(num)
            plus += int(num)
            
        return prod - plus