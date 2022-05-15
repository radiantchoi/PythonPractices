# 백준 온라인 저지 2675번 문자열 반복

n = int(input())

for _ in range(n):
    times, data = input().split()
    times = int(times)

    result = ""
    for letter in data:
        result += (letter * times)
    
    print(result)