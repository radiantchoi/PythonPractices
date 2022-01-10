# LeetCode No.739 Daily Temperatures

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                answer[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)

        return answer

# 여기서 스택에 넣는 것은 인덱스 즉, '일차'를 나타내는 수인 것이다. 온도값이 아니라.