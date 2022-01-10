# LeetCode No.1561 Maximum Numbers of Coins You Can Get

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        
        alice = 0
        me = 0
        bob = 0
        
        while len(piles) > 3:
            alice += piles[-1]
            me += piles[-2]
            bob += piles[0]
            
            del piles[0]
            del piles[-1]
            del piles[-2]
        
        me += piles[1]
        
        return me

# 시간복잡도 측면에서 봤을 때 이렇게 리스트에 직접 접근해서 뜯어내는 건 썩 좋은 방법은 아닌 것 같다.