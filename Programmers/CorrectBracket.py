# 프로그래머스 코딩테스트 연습 레벨 2 올바른 괄호

def solution(s):
    stack = []
    
    if s[0] == ")": # 없어도 되지만, 이 케이스에 걸리면 매우 효율적
        return False
    else:
        if s[-1] == "(":
            return False
    
    for i in range(len(s)):
        if not stack: # 스택이 비어있을 경우 - 즉 아직 괄호를 열지 않았을 경우
            if s[i] == ")":
                return False
            else:
                stack.append(s[i])
        else: # 스택이 비어있지 않을 경우 - 괄호를 이미 열었을 경우
            if s[i] == ")": # 이렇게 생각하니까 이 부분은 조금 지저분하다
                if stack[-1] == "(":
                    stack.pop()
            else:
                stack.append(s[i]) # 열었다가 또 열 수도 있으니까 아무튼 끝에 가서 다 닫히기만 하면 된다
    
    if len(stack) != 0: # 사실상 안닫힌 녀석이 있다는 말
        return False
            
    return True

# 문제에서 요구하는 조건을 잘 읽자. 이번 같은 경우는, 먼저 열고 그다음에 닫아야 한다는 말이 키 포인트였다.