# 백준 온라인 저지 1110번 더하기 사이클

initial = int(input())
n = initial
result = 0

while True:
    if n < 10:
        n *= 10
    
    a = n // 10 # 첫 번째 자리수
    b = n % 10 # 두 번째 자리수
    p = a + b # 이 두 개를 더한 것

    n = (b * 10) + (p % 10) # 두 번째 자리수는 10의 자리, 둘을 더해 나온 수의 일의 자리
    result += 1
    if n == initial:
        break

print(result)

# 스트링 자료형을 자르고 붙이는 것이라고 생각했지만, 수학적 센스로 접근하면 되는 것이었다..