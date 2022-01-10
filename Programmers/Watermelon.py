# 프로그래머스 코딩테스트 연습 레벨 1 수박수박수?

def solution(n):
    answer = []
    for i in range(n):
        if i % 2 == 0:
            answer.append("수")
        else:
            answer.append("박")
    
    return "".join(answer)

# join 함수는 리스트가 있을 때만 쓸 수 있음을 기억하자. 그냥 문자열을 위한 함수가 아냐.