# LeetCode No.260 Single Number III

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        numbers = {int: int}
        answer = []
        
        for n in nums:
            if n in numbers.keys():
                numbers[n] += 1
            else:
                numbers[n] = 1
        
        for key, value in numbers.items():
            if value == 1:
                answer.append(key)
        
        return answer

# 몰랐던 것 : 딕셔너리의 items, 괄호 안쳐도 되는 key value