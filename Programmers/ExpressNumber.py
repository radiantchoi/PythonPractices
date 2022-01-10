# 프로그래머스 코딩테스트 연습 레벨 2 숫자의 표현

def solution(n):
    answer = 0
    
    for m in range(1, n+1):
        holder = 0
        x = m
        while holder < n:
            holder += x
            x += 1
            if holder == n:
                answer += 1
                break
            elif holder > n:
                break
                
    return answer

# 의외로 시간복잡도도 잘 나옴
# 값을 들고 있는 holder 변수를 전역 변수로 하지 말고 for문 안에 넣으면 매번 초기화하지 않아도 된다