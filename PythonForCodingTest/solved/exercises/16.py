# 이것이 취업을 위한 코딩 테스트다 p.341 연구소
# 백준 온라인 저지 주소 : https://www.acmicpc.net/problem/14502

from itertools import combinations

height, width = map(int, input().split())
grid = []
for _ in range(height):
    row = list(map(int, input().split()))
    grid.append(row)

# 1회차 실패
# 잘 한 점 : 핵심 아이디어를 잘 캐치한 점. 경우의 수가 적기 때문에, 모든 경우를 탐색할 수 있다.
# 또, 스텝 바이 스텝으로 쪼개고 각 스텝에 대한 알고리즘을 작성한 것은 좋은 점.
# 개선해야 할 점 : 파이썬 구조에 대한 이해 부족, 탐색 알고리즘을 정확히 작성하지 못함
# 스위프트였으면 함수를 단위별로 쪼개고 inout 사용해서 해결해버렸을 것이다.
# while을 돌리는 지점에서 재귀 깊이 초과 오류가 발생했는데, 재귀 및 종료조건에 대해 생각해봐야 할 듯 하다.
# dfs bfs 상관없는 문제라, 하나만 제대로 할 줄 알아도 풀릴 것 같다. 90퍼센트는 풀었다고 본다.



# # 바이러스가 있는 칸 표시
# # 빈 칸 표시 (조합 구하기 위함)
# blanks = []
# viruses = []
# for i in range(height):
#     for j in range(width):
#         if grid[i][j] == 0:
#             blanks.append((i, j))
#         elif grid[i][j] == 2:
#             viruses.append((i, j))

# safeareas = []

# # 빈 칸에 선택한 좌표에다가 벽 세우기
# selections = list(combinations(blanks, 3))
# for selection in selections:
#     lab = grid
#     for point in selection:
#         lab[point[0]][point[1]] = 1

#     # 퍼지는 것 시뮬레이션하기
#     def traverse(y, x):
#         if y < 0 and y >= len(lab) and x < 0 and x >= len(lab[0]) and lab[y][x] != 0:
#             return
        
#         lab[y][x] = 2

#         traverse(y-1, x)
#         traverse(y+1, x)
#         traverse(y, x-1)
#         traverse(y, x+1)
    
#     for virus in viruses:
#         a = virus[0]
#         b = virus[1]

#         traverse(a+1, b)
#         traverse(a-1, b)
#         traverse(a, b-1)
#         traverse(a, b+1)

#     # 안전 영역 카운팅하기
#     safe = 0
#     for k in range(height):
#         for l in range(width):
#             if lab[k][l] == 0:
#                 safe += 1
    
#     safeareas.append(safe)

# # 안전 영역들 중 가장 큰 것 반환하기
# print(max(safeareas))