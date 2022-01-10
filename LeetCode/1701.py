# LeetCode No.1701 Average Waiting Time

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total = 0
        time = 0
        
        for customer in customers:
            if customer[0] > time:
                time = customer[0]
                total += customer[1]
            else:
                wait = customer[1] + (time - customer[0])
                total += wait
            time += customer[1]
        
        return total/len(customers)

# 파이썬이 이렇게 편합니다~ 자료형 지정해줄 필요도 없고