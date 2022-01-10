# 프로그래머스 코딩테스트 연습 레벨 2 점프와 순간이동
# 참고한 풀이 : https://inspirit941.tistory.com/232

def solution(n):
    count = 0
    
    while n > 0:
        a = n // 2
        b = n % 2
        
        n = a
        count += b
    
    return count

# 지금까지 간 거의 2배를 갈 수 있는게 순간이동이니까 순간이동 위주로 하게 된다.
# 그리디라고 생각은 했는데 거기에 매몰돼서 해법을 빨리 건지지 못했다.
# 역으로 주어진 수를 2로 나누는 게 순간이동, 나머지로 나오는 1을 더해주는 게 앞으로 점프한 횟수인 것.

def solution(n):
    return bin(n)[2:].count("1")

# 굉장히 기발한 풀이도 봤는데, n을 이진수로 바꾼 다음 1의 갯수를 세는 것이었다.
# 이진수는 0 또는 1이 곧 2로 나눈 나머지니까, 합리적인 추론