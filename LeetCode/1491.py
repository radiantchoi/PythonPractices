# LeetCode No.1491 Average Salary Excluding the Minimum and Maximum Salary
class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary.pop()
        salary.sort(reverse = True)
        salary.pop()
        return sum(salary) / len(salary)