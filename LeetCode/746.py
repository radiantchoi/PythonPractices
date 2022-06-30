# LeetCode No.746 Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        gross = cost[:2]
        
        if len(cost) > 2:
            for i in range(2, len(cost)):
                gross.append(cost[i] + min(gross[i-1], gross[i-2]))
                
        return min(gross[-1], gross[-2])

# dp 감잡기!