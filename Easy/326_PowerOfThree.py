"""
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.
"""



import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n>0 and (math.log10(n)/math.log10(3)).is_integer()