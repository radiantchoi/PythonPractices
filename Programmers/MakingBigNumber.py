# 프로그래머스 코딩테스트 연습 그리디 레벨 2 큰 수 만들기

def solution(number, k): # 스택을 이용해 푸는 방법. 다른 사람의 풀이 1번을 가져왔고, 이해하기 위해 풀이를 작성
    stack = []
    stack.append(number[0]) # 주어진 숫자의 첫 번째 자리를 스택에 입력
    for i in number[1:]: 
        while len(stack) > 0 and stack[-1] < i and k > 0: #len(stack)은 없어도 되지 않을까? 
            # 들어올 숫자가 스택의 마지막 숫자보다 큰 경우 / k 횟수 세기
            k -= 1 # k번 숫자를 제거해야 되니까 카운트 기능을 위해 넣어 준다
            stack.pop() # number에 남아 있는 숫자가 스택에 이미 있는 숫자보다 크니까 빼 주기
        stack.append(i) # 스택에 number에 남아 있는 숫자를 더해 준다
    if k != 0:
        stack = stack[:-k] # number = 10000, k = 2같은 케이스를 방지하기 위함이라고 한다
    answer = ''.join(stack)
    return answer