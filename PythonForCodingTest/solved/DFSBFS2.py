# 이것이 취업을 위한 코딩 테스트다 p.152 미로 탈출
from collections import deque

n, m = map(int, input().split())
grid = []
for _ in range(n):
    row = list(map(int, input()))
    grid.append(row)

def solution(n, m, grid):
    result = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        while queue:
            x, y = queue.popLeft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue

                if grid[nx][ny] == 0:
                    continue

                if grid[nx][ny] == 1:
                    grid[nx][ny] = grid[x][y] + 1
                    queue.append((nx, ny))
    
        return grid[n-1][m-1]

    return bfs(0, 0)

print(solution(n, m, grid))

# bfs는 이런 식으로 하는구나.. 하는 것을 잘 봐 두자.
# 키워드는 큐와 while, dx dy라고 생각된다.
