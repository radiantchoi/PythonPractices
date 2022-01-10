# LeetCode No.287 Find the Duplicate Number

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counting = {}
        
        for n in nums:
            if n not in counting:
                counting[n] = 1
            else:
                counting[n] += 1
            
        for key in counting:
            if counting[key] > 1:
                return key

# 드디어 딕셔너리를 조금 다룰 수 있게 됐나?