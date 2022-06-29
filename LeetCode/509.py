# LeetCode No.509 Fibonacci Number
# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        fibo = [0, 1]
        
        if n >= 2:
            for i in range(2, n+1):
                fibo.append(fibo[i-2] + fibo[i-1])
                
        return fibo[n]

# 짱쉬움