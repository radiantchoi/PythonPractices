# LeetCode No.1630 Arithmetic Subarrays

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n = len(nums)
        m = len(l)
        answer = [True] * m
        
        for i in range(m):
            arith = nums[l[i]:r[i]+1]
            arith.sort()
            for j in range(1, len(arith)-1):
                if arith[j] - arith[j-1] != arith[j+1] - arith[j]:
                    answer[i] = False
        
        return answer