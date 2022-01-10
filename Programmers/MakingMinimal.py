# 프로그래머스 코딩테스트 연습 레벨 2 최솟값 만들기

def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse=True)
    
    while A:
        x = A.pop()
        y = B.pop()
        answer += x*y

    return answer

# 솔직히 찍어맞춘 감이 있다.
# 문제의 예시 케이스를 보고 A의 가장 작은 것과 B의 가장 큰 것을 곱하면 더했을 때 최솟값이 된다고 생각했다.
# sort를 뒤집으려면 reversed가 아니라 reverse임을 유념하자.