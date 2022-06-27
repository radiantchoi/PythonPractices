# LeetCode No.1020 Number of Enclaves
# https://leetcode.com/problems/number-of-enclaves/

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        result = 0

        def traverse(r, c, n, m, grid):
            if r < 0 or r >= n or c < 0 or c >= m or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            grid[:] = grid
            
            area = 1
            
            dr = [-1, 1, 0, 0]
            dc = [0, 0, -1, 1]
            
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                
                area += traverse(nr, nc, n, m, grid)
            
            return area
        
        for i in range(n):
            for j in range(m):
                if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                    if grid[i][j] == 1:
                        traverse(i, j, n, m, grid)
                
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    area = traverse(i, j, n, m, grid)
                    result += area
        
        return result
            