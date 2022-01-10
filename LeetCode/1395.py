# LeetCode No.1395 Count Number of Teams

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        answer = 0
        
        for j in range(1, len(rating)-1):
            smalleri = 0
            largerk = 0
            
            largeri = 0
            smallerk = 0
            
            for i in range(j):
                if rating[i] < rating[j]:
                    smalleri += 1
                elif rating[i] > rating[j]:
                    largeri += 1
                
            for k in range(j+1, len(rating)):
                if rating[k] < rating[j]:
                    smallerk += 1
                elif rating[k] > rating[j]:
                    largerk += 1
            
            answer += (smalleri * largerk) + (largeri * smallerk)
            
        return answer
    
# 과거 스위프트 코드를 살짝 보고 감이 왔다.
# 역시, 1씩 더하는 과정을 수학적으로 줄여주기만 해도 시간이 훨씬 덜 걸린다.