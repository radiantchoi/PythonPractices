# LeetCode No.35 Search Insert Position
# https://leetcode.com/problems/search-insert-position/

from bisect import bisect_left

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)

# swift로 풀 때는 개고생했는데..