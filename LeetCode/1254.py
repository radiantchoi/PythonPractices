# LeetCode No.1254 Number of Closed Islands
# https://leetcode.com/problems/number-of-closed-islands/

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        result = 0
        
        def traverse(r, c, n, m, grid):
            if r < 0 or r >= n or c < 0 or c >= m or grid[r][c] == 1:
                return
            
            grid[r][c] = 1
            grid[:] = grid
            
            dr = [-1, 1, 0, 0]
            dc = [0, 0, -1, 1]
            
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                
                traverse(nr, nc, n, m, grid)
        
        for i in range(n):
            for j in range(m):
                if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                    if grid[i][j] == 0:
                        traverse(i, j, n, m, grid)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    traverse(i, j, n, m, grid)
                    result += 1
        
        return result