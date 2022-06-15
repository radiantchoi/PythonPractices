# LeetCode No.1283 Find the Smallest Divisor Given a Threshold
# 참고한 풀이 : https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/discuss/446376/JavaC%2B%2BPython-Binary-Search

# 처음 풀이 - 안 될 줄 알고 있었음
from math import ceil

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        divisor = 1
        
        while True:
            divs = [ceil(x / divisor) for x in nums]
            
            if sum(divs) > threshold:
                divisor += 1
            else:
                break
        
        return divisor
# 왜 그렇게 생각했냐면 이건 O(n^2)였거든

# 참고해서 푼 풀이
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        
        while left < right:
            mid = (left + right) // 2
            if sum(ceil(num / mid) for num in nums) > threshold:
                left = mid + 1
            else:
                right = mid
        
        return left
# divisor의 값 자체에만 집중하면 됐던 거지..
# divisor를 이진 탐색으로 찾아내는 거였다.