# 프로그래머스 코딩테스트 연습 레벨 1 서울에서 김서방 찾기

def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            return "김서방은 %d에 있다" % i

# %를 활용한 문자열 포매팅에 대해 다시 봐야 할 듯 하다. 스위프트의 \()에 너무 익숙해졌음