# LeetCode No.1502 Can Make Arithmetic Progression From Sequence

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        index = 2
        
        while index < len(arr):
            if arr[index-1] - arr[index-2] == arr[index] - arr[index-1]:
                index += 1
            else:
                return False
            
        return True