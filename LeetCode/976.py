# LeetCode No.976 Longest Perimeter Triangle

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        result = 0
        nums.sort(reverse = True)
        
        for i in range(len(nums)-2):
            slice = nums[i:i+3]
            if slice[0] >= slice[1] + slice[2]:
                continue
            else:
                result = sum(slice)
                break
            
        return result