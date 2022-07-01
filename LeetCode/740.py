# LeetCode No.740 Delete and Earn
# https://leetcode.com/problems/delete-and-earn/
# 참조 : https://leetcode.com/problems/delete-and-earn/solution/

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        gain = {}
        for n in nums:
            gain[n] = gain.get(n, 0) + n
            
        points = [0] * (max(nums) + 1)
        
        for key, value in gain.items():
            points[key] = value
        
        for i in range(min(nums), max(nums)+1):
            if i > 1:
                points[i] += max(points[:i-1])

        return max(points)

# i+1을 생각한다는 것도 일종의 함정이었다! 값을 저장할 때 i-1은 빼고 고려하면 결국 똑같은 문제였던 것.
# 이 경우 House Robber와 같은 유형의 문제이다.