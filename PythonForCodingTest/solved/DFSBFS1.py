# 이것이 취업을 위한 코딩 테스트다 p.149 음료수 얼려 먹기

n, m = map(int, input().split())
grid = []
for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

def solution(n, m, grid):
    result = 0
    visited = [[False] * m] * n

    def traverse(col, row, grid, visited):
        if col < 0 or col >= n or row < 0 or row >= m or visited[col][row] == True or grid[col][row] == 1:
            return False
        
        visited[col][row] == True

        traverse(col+1, row, grid, visited)
        traverse(col-1, row, grid, visited)
        traverse(col, row+1, grid, visited)
        traverse(col, row-1, grid, visited) # 여기서 나오는 True들은 다 버려진다 - 단지 방문했다고 마크만 될 뿐
        return True

    for i in range(n):
        for j in range(m):
            if traverse(i, j, grid, visited) == True:
                result += 1
    
    return result

print(solution(n, m, grid))

# 탈출 조건에 대해 인지하지 못했었다. 왜 True를 반환해야 했을까? 에 대한 물음
# 해결! 하나 콕 찍으면 True가 반환이 되고, 이미 방문한 곳은 False를 반환하게 설계했기 때문.
# 결과적으로, 이어지지 않은 구멍의 수만 셀 수 있다.