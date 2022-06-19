# LeetCode No.283 Move Zeroes
# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        z = nums.count(0)
        new = [n for n in nums if n != 0]
        zeroes = [0] * z
        nums[:] = new + zeroes