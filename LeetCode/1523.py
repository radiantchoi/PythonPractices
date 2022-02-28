# LeetCode No.1523 Count Odd Numbers in an Interval Range

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        numbers = high - low + 1
        if numbers % 2 == 0:
            return int(numbers / 2)
        else:
            cut = int((numbers - 1) / 2)
            if low % 2 == 1:
                return cut + 1
            else:
                return cut