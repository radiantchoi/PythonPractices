# 백준 온라인 저지 1193번 분수 찾기

n = int(input())

triangle = [0]
level = 1
while triangle[-1] < n:
    triangle.append(triangle[-1] + level)
    level += 1

diff = triangle[-1] - n

if level % 2 == 0:
    x = 1 + diff
    y = (level - 1) - diff
    print("%d/%d" % (x, y))
else:
    x = (level - 1) - diff
    y = 1 + diff
    print("%d/%d" % (x, y))
