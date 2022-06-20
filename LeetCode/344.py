# LeetCode No.344 Reverse String
# https://leetcode.com/problems/reverse-string/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]