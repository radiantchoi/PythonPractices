# LeetCode No.1779 Find Nearest Point That Has the Same X or Y Coordinate

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        result = -1
        dist = 10001
        
        for point in points:
            if point[0] == x or point[1] == y:
                current = abs(x - point[0]) + abs(y - point[1])
                if current < dist:
                    dist = current
                    result = points.index(point)
            else:
                continue
        
        return result

# 알아둘 것 : 리스트.index(원소). 파이썬에서는 인덱스 알아내기가 이렇게 편합니다