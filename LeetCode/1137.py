# LeetCode No.1137 N-th Tribonacci Number
# https://leetcode.com/problems/n-th-tribonacci-number/

class Solution:
    def tribonacci(self, n: int) -> int:
        tribo = [0, 1, 1]
        
        if n >= 3:
            for i in range(3, n+1):
                tribo.append(tribo[i-3] + tribo[i-2] + tribo[i-1])
        
        return tribo[n]

# 꽤 쉬움