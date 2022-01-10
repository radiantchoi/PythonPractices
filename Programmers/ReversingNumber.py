# 프로그래머스 코딩테스트 연습 레벨 1 자연수 뒤집어 배열로 만들기

def solution(n):
    answer = list(str(n))
    answer.reverse()
    
    for i in range(len(answer)):
        answer[i] = int(answer[i])
        
    return answer

# 다른 사람의 풀이를 보니, 한 줄에 깔끔하게 끝낸 코드도 있었다.
# 하지만 지금 내 입장에선, 코드가 굳이 파이써닉해야 할 필요도 없고, 이해하는 대로 사용하면 된다.
# 그래서 알아보기 쉬운 코드가 가치를 가진다고 생각한다.