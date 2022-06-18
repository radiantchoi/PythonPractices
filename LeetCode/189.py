# LeetCode No.189 Rotate Array
# https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        move = k % length
        new = nums + nums
        
        nums[:] = new[length-move:(2*length)-move]

# nums와 nums[:]의 차이!! 중요!! inout에 대한 좋은 솔루션!!!