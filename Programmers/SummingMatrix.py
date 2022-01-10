# 프로그래머스 코딩테스트 연습 레벨 1 행렬의 덧셈

def solution(arr1, arr2):
    answer = arr1
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            answer[i][j] += arr2[i][j]
            
    return answer

# 순발력이 조금은 는 것 같다.