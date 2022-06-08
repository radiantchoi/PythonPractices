# 이것이 취업을 위한 코딩 테스트다 p.359 국영수
# 백준 온라인 저지 주소 : https://www.acmicpc.net/problem/10825
# 제한시간 20분

students = int(input())
scores = []
for _ in range(students):
    name, korean, english, math = input().split()
    card = (name, int(korean), int(english), int(math))
    scores.append(card)

scores.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))
for score in scores:
    print(score[0])

# 여러 가지 조건을 정해서 정렬하는 법만 알아두자!