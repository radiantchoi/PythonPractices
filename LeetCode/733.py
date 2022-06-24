# LeetCode No.733 Flood Fill
# https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        prevColor = image[sr][sc]
        
        def traverse(prev, new, row, col, image):
            if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]) or prev == new or image[row][col] != prev:
                return
            
            image[row][col] = new
            image[:] = image # 이 부분을 적극 활용해봤다
            
            dy = [-1, 1, 0, 0]
            dx = [0, 0, -1, 1]
            
            for i in range(4):
                ny = row + dy[i]
                nx = col + dx[i]
                traverse(prev, new, ny, nx, image)
            
        traverse(prevColor, newColor, sr, sc, image)
        
        return image