arr = list(map(int, input().split()))
arr.sort()
result = [0] * (max(arr)+1)

for number in arr:
    result[number] += 1

while 0 in result:
    result.remove(0)

while 1 in result:
    result.remove(1)

if result:
    print(result)
else:
    result.append(-1)
    print(result)
