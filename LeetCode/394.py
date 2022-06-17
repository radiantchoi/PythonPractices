# LeetCode No.394 Decode String

class Solution:
    def decodeString(self, s: str) -> str:
        result = ""
        num = ""
        
        i = 0
        while i < len(s):
            if s[i].isalpha():
                result += s[i]
            elif s[i].isdecimal():
                num += s[i]
            else:
                stack = []
                snippet = ""
                
                stack.append(s[i])
                snippet += s[i]
                
                while stack:
                    i += 1
                    if s[i] == "[":
                        stack.append(s[i])
                        snippet += s[i]
                    elif s[i] == "]":
                        stack.pop()
                        snippet += s[i]
                    else:
                        snippet += s[i]
                
                piece = snippet[1:len(snippet)-1]
                quote = self.decodeString(piece)
                
                if num:
                    result += quote * int(num)
                    num = ""
                else:
                    result += quote
            
            i += 1
                
        return result

# 재귀와 스택이라는 문제 장르를 보고 풀기는 했다.