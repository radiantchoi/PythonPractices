# LeetCode No.55 Jump Game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        stretch = nums[0]
        for i in range(len(nums)):
            if i > stretch:
                return False
            stretch = max(stretch, i + nums[i])
        
        return True