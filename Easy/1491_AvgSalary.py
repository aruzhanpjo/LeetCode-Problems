"""
You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.
"""


# beats - 77.15%, runtime - 44ms, memory - 69.28% beats
class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        theSum = float(sum(salary)-(salary[0]+salary[-1]))
        theLen = float(len(salary)-2)

        return theSum/theLen
        
