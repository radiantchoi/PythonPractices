# LeetCode No.191 Number of 1 Bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)[2:]
        bits = list(binary)
        count = 0
        for bit in bits:
            if bit == "1":
                count += 1
        
        return count

# 알아둘 것: 진수 변환(bin) - 이 경우 앞의 두 자리는 진수를 나타내는 식별자가 붙으니까, 떼어내자.
# 2진수는 0b, 8진수는 0o, 16진수는 0x이며, 각각 bin oct hex이다.