# 이것이 취업을 위한 코딩 테스트다 p.180 성적이 낮은 순서로 학생 출력하기

n = int(input())
scores = []
for _ in range(n):
    name, score = input().split()
    scores.append((name, int(score)))

def solution(scores):
    scores.sort(key=lambda x: x[1])
    return scores

for score in scores:
    print(score[0], end=" ")