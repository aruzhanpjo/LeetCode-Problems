"""
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
"""

class Solution:
    def addDigits(self, num: int) -> int:
        
        while num>=9:
            sum=(num%10)+(num//10)

            if sum<10:
                return sum
            else:
                return self.addDigits(sum)

        else:
            return num
