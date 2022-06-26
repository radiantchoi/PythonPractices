# LeetCode No.695 Max Area of Island
# https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        result = 0
        
        def traverse(r, c, n, m, grid):
            if r < 0 or r >= n or c < 0 or c >= m or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            grid[:] = grid
            area = 1
            
            dy = [-1, 1, 0, 0]
            dx = [0, 0, -1, 1]
            
            for i in range(4):
                nr = r + dy[i]
                nc = c + dx[i]
                
                area += traverse(nr, nc, n, m, grid)
            
            return area
            
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    res = traverse(i, j, n, m, grid)
                    result = max(res, result)
                    
        return result
        