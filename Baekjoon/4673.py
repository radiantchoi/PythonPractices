# 백준 온라인 저지 4673번 셀프 넘버

def d(n) -> int:
    plus = n
    digits = str(n)
    for digit in digits:
        plus += int(digit)
    
    return plus

def self_number() -> list:
    numbers = [True] * 10001

    for i in range(1, len(numbers)):
        new = d(i)
        if new >= len(numbers):
            continue

        numbers[new] = False
    
    return numbers

result = self_number()
for i in range(1, len(result)):
    if result[i] == True:
        print(i)
