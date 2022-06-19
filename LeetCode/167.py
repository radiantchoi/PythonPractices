# LeetCode No.167 Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers)-1

        while start < end:
            n = numbers[start] + numbers[end]
            if n == target:
                break
            elif n > target:
                end -= 1
            else:
                start += 1
                
        return [start + 1, end + 1]