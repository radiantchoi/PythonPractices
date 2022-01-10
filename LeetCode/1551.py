# LeetCode No.1551 Minimum Operations to Make Array Equal

class Solution:
    def minOperations(self, n: int) -> int:
        answer = 0
        result = []
        for i in range(n):
            result.append(2*i + 1)
        
        x = 0
        y = n-1
        while x <= y:
            answer += (result[x] + result[y])/2 - result[x]
            x += 1
            y -= 1
        
        return int(answer)
