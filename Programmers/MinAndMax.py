# 프로그래머스 코딩테스트 연습 레벨 2 최댓값과 최솟값

def solution(s):
    answer = ''
    
    letters = list(s.split())
    numbers = []
    for letter in letters:
        numbers.append(int(letter))
    
    answer += str(min(numbers))
    answer += " "
    answer += str(max(numbers))
        
    return answer

# split()이 여기서도 통하는구나 알 수 있었던 좋은 시간이었습니다.