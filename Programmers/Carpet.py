# 프로그래머스 코딩테스트 연습 완전탐색 레벨 2 카펫

def solution(brown, yellow):
    answer = []
    if yellow == 1:
        answer = [3, 3]
    else:
        for i in range(1, yellow):
            height = i + 2 # 노랑색 영역을 감싸는 모양새이므로
            width = yellow / (height - 2) + 2 # 어찌 보면 노랑을 나누어 떨어지게 하는 수가 높이-2 가 될 수 있다
            if width >= height and brown == 2*(height-2) + 2*width: # 조건을 이렇게 마구잡이로 잡아도 된다니
                answer.append(width)
                answer.append(height)

    return answer

# 방정식을 세워서 풀었다. 이미 자력으로 푼 경험이 있기 때문에, 언어만 바꿔 보았다.