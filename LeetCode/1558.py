# LeetCode No.1558 Minimum Numbers of Function Calls to Make Target Array

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        
        for n in nums:
            if n != 0:
                count += 1
        
        nums.sort()
        lead = nums.pop()
        while lead > 1:
            if lead % 2 == 0:
                lead /= 2
                count += 1
            else:
                lead -= 1
                count += 1
        
        for m in nums:
            while m > 1:
                if m % 2 == 1:
                    m -= 1
                    count += 1
                else:
                    m /= 2
        
        return count