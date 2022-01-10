# 프로그래머스 코딩테스트 연습 레벨 2 짝지어 제거하기
# 참고한 풀이 : https://eda-ai-lab.tistory.com/492

def solution(s):
    stack = []
    
    for letter in s:
        if len(stack) == 0:
            stack.append(letter)
        elif stack[-1] == letter:
            stack.pop()
        else: 
            stack.append(letter)
    
    if len(stack) == 0:
        return 1
    else:
        return 0

# 문자열을 직접 건드리거나 리스트로 만들지 않고, 스택을 활용해 짝지어 제거하는 방법.
# 문자열, 짝짓기 키워드가 나오면 스택을 활용하는 것을 생각해 봐야겠다.