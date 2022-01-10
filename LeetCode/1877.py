# LeetCode No.1877 Minimize Maximum Pair Sum in Array

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = []
        
        i = 0
        j = len(nums)-1
        
        while i < j:
            result.append(nums[i] + nums[j])
            i += 1
            j -= 1
        
        return max(result)