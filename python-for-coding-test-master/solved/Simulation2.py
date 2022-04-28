# 이것이 취업을 위한 코딩 테스트다 p.118 게임 개발

row, col = map(int, input().split())
pos = list(map(int, input().split()))
grid = []
for i in range(col):
    grid.append(list(map(int, input().split())))

def solution(pos, grid, row, col):
    y = pos[0]
    x = pos[1]
    dir = pos[2]
    visited = [[False] * 8] * 8
    visited[y][x] = True
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    result = 1
    turned = 0
    while True:
        dir -= 1
        if dir == -1:
            dir = 3
        
        ny = y + moves[dir][0]
        nx = x + moves[dir][1]
        if nx >= 0 and nx < row and ny >= 0 and ny < col and visited[ny][nx] == False and grid[ny][nx] == 0:
            y = ny
            x = nx
            result += 1
            visited[ny][nx] = True
            turned = 0
        else:
            if turned < 4:
                turned += 1
            else:
                back = (dir + 2) % 4
                by = y + moves[back][0]
                bx = x + moves[back][1]
                if by < 0 or by >= col or bx < 0 or bx >= row or grid[by][bx] == 1:
                    break
                else:
                    y = by
                    x = bx
                    turned = 0

    return result

# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1

print(solution(pos, grid, row, col))