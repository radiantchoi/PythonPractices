# 이것이 취업을 위한 코딩 테스트다 p.96 숫자 카드 게임

n, m = map(int, input().split())
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))

def solution(n, m, grid) -> int:
    maximum = 0

    for i in range(len(grid)):
        maximum = max(maximum, min(grid[i]))
    
    return maximum

print(solution(n, m, grid))
