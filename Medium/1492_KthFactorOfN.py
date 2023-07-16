"""
You are given two positive integers n and k. A factor of an integer n is defined as an integer i where n % i == 0.

Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 
if n has less than k factors.
"""


#runtime - 37ms, beats - 97.41%, memory - 73.70%
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        count=0
        i=1
        while i<=n:
            if n%i == 0:
                count+=1
                if count==k:
                    return i 
            
            i+=1
        return -1


