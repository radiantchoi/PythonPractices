# 프로그래머스 코딩테스트 연습 레벨 2 다음 큰 숫자
# 참고한 풀이 : https://hocheon.tistory.com/100

def solution(n):
    answer = 0
    counting = bin(n).count('1')
    
    for m in range(n+1, 1000001):
        if bin(m).count('1') == counting:
            answer = m
            break
    
    return answer

# 알아둘 것이 몇 가지 있다.
# 먼저 bin, oct 등의 진법 함수들은 결과물을 String 형태로 뱉어낸다. 인덱싱이 가능하다는 말이다.
# 다음으로 count() 함수는 리스트와 스트링에 쓸 수 있으며 특정 요소의 갯수를 세 준다.