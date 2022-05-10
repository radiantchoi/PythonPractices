# 백준 온라인 저지 1546번 평균

n = int(input())
points = list(map(int, input().split()))

base = max(points)
crack = []
for point in points:
    crack.append(point / base * 100)

print(sum(crack) / len(crack))