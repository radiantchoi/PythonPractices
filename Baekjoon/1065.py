# 백준 온라인 저지 1065번 한수

def hansu(n) -> bool:
    data = list(str(n))
    if len(data) < 3:
        return True
    
    digits = [int(x) for x in data]

    for i in range(1, len(digits)-1):
        if (digits[i] - digits[i-1]) != (digits[i+1] - digits[i]):
            return False
    
    return True

n = int(input())
result = 0
for i in range(1, n+1):
    if hansu(i):
        result += 1

print(result)