# LeetCode No.1992 Find All Groups of Farmland
# https://leetcode.com/problems/find-all-groups-of-farmland/

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        result = []
        
        def traverse(row, col, grid, points):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 0:
                return
            
            points.append([row, col])
            grid[row][col] = 0
            
            dy = [-1, 1, 0, 0]
            dx = [0, 0, -1, 1]
            
            for i in range(4):
                ny = row + dy[i]
                nx = col + dx[i]
                traverse(ny, nx, grid, points)
            
        for i in range(len(land)):
            for j in range(len(land[i])):
                points = []
                traverse(i, j, land, points)
                points.sort(key = lambda x: (x[0], x[1]))
                if points:
                    territory = points[0] + points[-1]
                    result.append(territory)
        
        return result