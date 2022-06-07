# 이것이 취업을 위한 코딩 테스트다 p.327 뱀
# 백준 온라인 저지 주소 : https://www.acmicpc.net/problem/3190

# 1회차 실패
# 잘 한 점 : 거의 다..? 일단 경우의 수를 다 잘 찾아냈다. 이동하는 것도 잘 이해했다.
# 개선해야 할 점 : 뱀의 머리와 꼬리만 쫓았다는 거. 명확히 풀이하기 위해, 뱀의 몸통 정보도 저장하는 것이 좋아 보인다.
# 또한 이렇게 데이터가 많은 문제는, 데이터를 올바르게 처리하고 있는지도 계속 추적해야 한다.

# from collections import deque

# n = int(input())
# apples = int(input())
# locations = []
# for _ in range(apples):
#     locations.append(list(map(int, input().split())))
# turned = int(input())
# turns = []
# for _ in range(turned):
#     turn = list(input().split())
#     turn[0] = int(turn[0])
#     turns.append(turn)

# grid = [[0] * n] * n
# for apple in locations:
#     grid[apple[1]-1][apple[0]-1] = 1

# def solution(grid, turns):
#     head = [0, 0] # y, x
#     tail = [0, 0]
#     heading = 0
#     tailing = 0
#     length = 1
#     grid[head[0]][head[1]] = 2
#     grid[tail[0]][tail[1]] = 2

#     headnavi = deque(turns)
#     tailnavi = deque(turns)

#     dx = [1, 0, -1, 0] # R D L U
#     dy = [0, 1, 0, -1]

#     est = 0
#     while True:
#         est += 1
        
#         if headnavi and est == headnavi[0][0]:
#             headnext = headnavi.popleft()
#             heading = direction(headnext[1])

#         nhy = head[0] + dy[heading]
#         nhx = head[1] + dx[heading]

#         if nhy < 0 or nhy >= len(grid) or nhx < 0 or nhx >= len(grid[0]):
#             break

#         if grid[nhy][nhx] == 1:
#             grid[nhy][nhx] = 2
#             head = [nhy, nhx]
#             length += 1
#         elif grid[nhy][nhx] == 2:
#             break
#         else:
#             grid[nhy][nhx] = 2
#             head = [nhy, nhx]

#             grid[tail[0]][tail[1]] = 0
#             if tailnavi and est == tailnavi[0][0] + length - 1:
#                 tailnext = tailnavi.popleft()
#                 tailing = direction(tailnext[1])

#             nty = tail[0] + dy[tailing]
#             ntx = tail[1] + dx[tailing]
#             tail = [nty, ntx]
            
#     return est

# def direction(a):
#     if a == "R":
#         return 0
#     elif a == "D":
#         return 1
#     elif a == "L":
#         return 2
#     else:
#         return 3
    
# result = solution(grid, turns)
# print(result)