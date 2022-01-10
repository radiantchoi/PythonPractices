# 프로그래머스 코딩테스트 연습 레벨 2 전화번호 목록
# 참고한 풀이 : https://velog.io/@chaegil15/프로그래머스파이썬-해시-전화번호-목록

def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i+1][:len(phone_book[i])] == phone_book[i]:
                answer = False
                break
                
    return answer

# 시간복잡도를 줄여 주려면, 신경쓸 것을 줄여 줘야 한다.
# 먼저 정렬을 통해, 같은 접두사를 가진 문자열이 앞으로 오도록 한다.
# 그 다음, 붙어있는 두 개가 길이가 서로 다르고 접두어가 같다면, false를 출력하는 방식. in을 쓰는 게 아닌 이유는 접두어기 때문
# 파이썬의 문자열 정렬 방식을 잘 알고 있었더라면 응용할 수 있었다. 