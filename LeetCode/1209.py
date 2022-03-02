# LeetCode No.1209 Remove All Adjacent Duplicates in String II

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for letter in s:
            if stack:
                if stack[-1][0] == letter:
                    stack[-1][1] += 1
                    if stack[-1][1] == k:
                        stack.pop()
                else:
                    stack.append([letter, 1])
            else:
                stack.append([letter, 1])
        
        return "".join(letter * n for letter, n in stack)

# 파이썬에서 문자열을 합치는 방법에 대해 다시 고민해보자.
# 저렇게 간단하게 두 가지 요소를 다룰 수 있다는 것은 감탄스럽다.