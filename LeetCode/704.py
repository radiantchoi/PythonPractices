# LeetCode No.704 Binary Search
# https://leetcode.com/problems/binary-search/

from bisect import bisect_left, bisect_right

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if bisect_left(nums, target) == bisect_right(nums, target):
            return -1
        else:
            return bisect_left(nums, target)