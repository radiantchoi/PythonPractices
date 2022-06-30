# LeetCode No.198 House Robber
# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        total = nums[:2]
        
        if len(nums) > 2:
            for i in range(2, len(nums)):
                new = nums[i] + max(total[:i-1])
                total.append(new)
        
        return max(total)

# 글쎄.. 그저 반복학습의 결과물이 아닌가?