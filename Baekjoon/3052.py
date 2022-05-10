# 백준 온라인 저지 3052번 나머지

leftovers = set()

for i in range(10):
    data = int(input()) % 42
    leftovers.add(data)

print(len(leftovers))