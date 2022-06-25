# LeetCode No.994 Retting Oranges
# https://leetcode.com/problems/rotting-oranges/

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        bads = []
        
        n = len(grid)
        m = len(grid[0])
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    bads.append((i, j, 0))
        
        progress = deque(bads)
        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]
        
        while progress:
            bad = progress.popleft()
            time = max(time, bad[2])
            
            for i in range(4):
                ny = bad[0] + dy[i]
                nx = bad[1] + dx[i]
                
                if ny >= 0 and ny < n and nx >= 0 and nx < m and grid[ny][nx] == 1:
                    grid[ny][nx] = 2
                    progress.append((ny, nx, bad[2] + 1))
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        
        return time