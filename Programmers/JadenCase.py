# 프로그래머스 코딩테스트 연습 레벨 2 JadenCase 문자열 만들기

def solution(s):
    holder = list(s)
    
    if holder[0].isalpha():
        holder[0] = holder[0].upper()
    
    for i in range(1, len(holder)):
        if holder[i].isalpha():
            if holder[i-1] == " ":
                holder[i] = holder[i].upper()
            else:
                holder[i] = holder[i].lower()
    
    return "".join(holder)

# 알아둬야 할 문법이 몇 가지 있다.
# 문자열을 전부 대문자로 바꾸는 것은 upper(), 반대는 lower()
# 첫 글자만 대문자로 바꾸는 건 capitalize(), 공백이나 숫자 등으로 구분되어 있는 매 단어를 바꾸려면 title()
# 함수를 적용해 리스트 요소를 바꾸는 것을 잘 쓰자. holder[i].upper()만 덜렁 써놓고 안바뀐다고 투덜대지 말고..