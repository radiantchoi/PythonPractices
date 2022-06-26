# LeetCode No.200 Number of Islands
# https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        result = 0
        
        def traverse(row, col, grid):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == "0":
                return
            
            grid[row][col] = "0"
            grid[:] = grid
            
            dy = [-1, 1, 0, 0]
            dx = [0, 0, -1, 1]
            
            for i in range(4):
                nr = row + dy[i]
                nc = col + dx[i]
                traverse(nr, nc, grid)
            
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    traverse(i, j, grid)
                    result += 1
        
        return result