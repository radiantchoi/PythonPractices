# 백준 온라인 저지 1110번 더하기 사이클

initial = input()
n = initial
result = 0

while True:
    if len(n) == 1:
        n += "0"
    
    plus = str(int(n[0]) + int(n[1]))
    n = n[1] + plus[-1]
    result += 1
    if n == initial:
        break

print(result)