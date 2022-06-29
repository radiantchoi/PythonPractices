# LeetCode No.70 Climing Stairs
# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        fibo = [1, 1, 2]
        
        if n >= 3:
            for i in range(3, n+1):
                fibo.append(fibo[i-2] + fibo[i-1])
        
        return fibo[n]

# DP 문제는 손으로 몇 번 구해보면서 점화식을 찾아내는 것이 중요하구나 생각이 들었다.