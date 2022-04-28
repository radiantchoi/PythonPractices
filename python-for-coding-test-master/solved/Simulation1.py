# 이것이 취업을 위한 코딩 테스트다 p.115 왕실의 나이트

pos = input()

def solution(pos):
    row = [0] * 8
    grid = []
    for i in range(8):
        grid.append(row)

    posrow = ord(pos[0]) - 97
    poscol = int(pos[1]) - 1

    result = 0
    movement = [[1, 2], [1, -2], [2, 1], [2, -1], [-1, 2], [-1, -2], [-2, 1], [-2, -1]]

    for move in movement:
        newrow = posrow + move[0]
        newcol = poscol + move[1]

        if newrow >= 0 and newrow < len(grid[0]) and newcol >= 0 and newcol < len(grid):
            result += 1

    return result

print(solution(pos)) 

# ord 사용할 경우, A는 65번 a는 97번인 것을 기억하자.