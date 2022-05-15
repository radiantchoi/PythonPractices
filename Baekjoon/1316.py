# 백준 온라인 저지 1316번 그룹 단어 체커

n = int(input())
result = 0

for _ in range(n):
    data = input()
    storage = []
    group = True
    for i in range(len(data)):
        if data[i] in storage:
            if data[i] != data[i-1]:
                group = False
                break
        else:
            storage.append(data[i])
        
    if group:
        result += 1

print(result)