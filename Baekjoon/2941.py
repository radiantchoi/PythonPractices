# 백준 온라인 저지 2941번 크로아티아 알파벳

data = input()
index = 0
check = ['c', 'd', 'l', 'n', 's', 'z']
croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
result = 0

while index < len(data):
    if data[index] in check:
        if index + 1 < len(data) and "".join(data[index:index+2]) in croatian:
            result += 1
            index += 2
        elif index + 2 < len(data) and "".join(data[index:index+3]) in croatian:
            result += 1
            index += 3
        else:
            result += 1
            index += 1
    else:
        result += 1
        index += 1

print(result)
