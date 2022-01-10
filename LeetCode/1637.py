# LeetCode No.1637 Widest Vertical Area Between Two Points Containing No Points

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xaxis = []
        
        for point in points:
            xaxis.append(point[0])
        
        xaxis.sort()
        
        diff = 0
        
        for i in range(1, len(xaxis)):
            if xaxis[i] - xaxis[i-1] > diff:
                diff = xaxis[i] - xaxis[i-1]
        
        return diff

# 스위프트보다 많이 빠르네 이게 어찌된 일이지?