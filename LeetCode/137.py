# LeetCode No.137 Single Number II

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        answer = 0
        
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        
        for key in count:
            if count[key] == 1:
                answer = key
                break
        
        return answer

# 딕셔너리에서 어떤 키에 대한 값을 찾을 때 굳이 keys()를 안 붙여도 된다 파이썬에선.