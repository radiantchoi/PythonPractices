# 백준 온라인 저지 5622번 다이얼

datas = list(input())

result = 0

for data in datas:
    n = ord(data)
    if n <= 67:
        result += 3
    elif n <= 70:
        result += 4
    elif n <= 73:
        result += 5
    elif n <= 76:
        result += 6
    elif n <= 79:
        result += 7
    elif n <= 83:
        result += 8
    elif n <= 86:
        result += 9
    else:
        result += 10

print(result)