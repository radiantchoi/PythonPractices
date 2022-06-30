# LeetCode No.213 House Robber II
# https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        first = nums[:len(nums)-1]
        second = nums[1:]
        
        if len(first) > 2:
            for i in range(2, len(first)):
                first[i] += max(first[:i-1])
        
        if len(second) > 2:
            for i in range(2, len(second)):
                second[i] += max(second[:i-1])
        
        return max(max(first), max(second))