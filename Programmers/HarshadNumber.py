# 프로그래머스 코딩테스트 연습 레벨 1 하샤드 수

def solution(x):
    data = list(str(x))
    digits = []
    for i in data:
        digits.append(int(i))
    divider = sum(digits)
    if x % divider == 0:
        return True
    else:
        return False

# 사실상 스위프트에서 map 활용해서 하던 것처럼, 들어오는 숫자를 문자열로 리스트에 뿌려주는 훈련.
# 단, 파이썬에서는 int로 바꿀 때 옵셔널을 강제 언래핑하지 않아도 된다는 차이가 있다.