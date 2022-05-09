# 백준 온라인 저지 2480번 주사위 세개

points = list(map(int, input().split()))
points.sort()
points_set = set(points)

if len(points_set) == 1:
    print(10000 + points[0] * 1000)
elif len(points_set) == 2:
    if points.count(points[0]) == 2:
        print(1000 + points[0] * 100)
    else:
        print(1000 + points[2] * 100)
else:
    print(points[2] * 100)