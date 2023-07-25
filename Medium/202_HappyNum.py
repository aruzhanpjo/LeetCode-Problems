"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
"""

#need to re-solve in a week or so, as the solution is from neetcode
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n not in visited:
            visited.add(n)
            n = self.summation(n)

            if n==1:
                return True

        return False

    def summation(self, n: int):
        out = 0

        while n:
            digit = n%10
            digit = digit ** 2
            out += digit
            n = n//10

        return out

