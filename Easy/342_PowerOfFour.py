"""
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.
"""

# used bit manipulation to see if it has a base of 2
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n>0 and n&(n-1)==0 and (sqrt(n))*(sqrt(n))==n