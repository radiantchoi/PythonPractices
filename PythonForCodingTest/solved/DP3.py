# 이것이 취업을 위한 코딩 테스트다 p.223 바닥 공사

n = int(input())

def solution(n):
    table = [0] * 1001
    table[1] = 1
    table[2] = 3

    for i in range(3, n+1):
        table[i] = table[i-1] + 2 * table[i-2] # 뒤의 한 칸까지 차 있을 경우(1가지) + 뒤의 두 칸까지 차 있을 경우(2가지)
        table[i] = table[i] % 796796

    return table[n]

print(solution(n))

# 접근 방식은 괜찮았는데, 계산 실수를 처음에 하는 바람에..
# 1칸, 그리고 2칸을 채울 때의 방법의 가짓수를 활용한 것은 아주 좋았다.
# 하지만 2칸을 채울 때의 가짓수를 잘못 계산하는 바람에 전체적으로 틀어졌다.
# 현실에 존재하는 관념을 점화식화하는 과정이 필요할 것 같다.