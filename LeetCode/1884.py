# LeetCode No.1884 Egg Drop With 2 Eggs and N Floors

class Solution:
    def twoEggDrop(self, n: int) -> int:
        pyramid = [1]
        
        while pyramid[-1] < n:
            pyramid.append(pyramid[-1] + len(pyramid) + 1)
        
        return len(pyramid)

# 이 문제가, x층에서 먼저 떨어뜨린 다음  x-1개의 가짓수, 뭐 그런 식으로 전개됐던 걸로 기억한다.