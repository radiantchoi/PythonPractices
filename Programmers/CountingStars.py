# 프로그래머스 코딩테스트 연습 레벨 1 직사각형 별찍기

a, b = map(int, input().strip().split(' '))
stars = "*" * a
count = 0
while count < b:
    print(stars)
    count += 1

# 아는 범위 안에서 야매로 해결하는 능력에 대해 돌아보게 되었다.