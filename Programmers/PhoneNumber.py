# 프로그래머스 코딩테스트 연습 레벨 1 핸드폰 번호 가리기

def solution(phone_number):
    numbers = list(str(phone_number))
    
    for i in range(len(numbers)-4):
        numbers[i] = "*"
    
    answer = "".join(numbers)
    return answer

# 스위프트 코딩할 때 자주 하던 습관대로 문자열에 뿌려주고 합치는 방법을 썼다.
# 스위프트에서는 배열.joined(), 파이썬에서는 "".join(리스트) 임을 기억하자