# 백준 온라인 저지 2292번 벌집

n = int(input())
times = 1
tiles = 1

while n > tiles:
    tiles += 6 * times
    times += 1

print(times)