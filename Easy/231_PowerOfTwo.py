"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:


# intuitive solution
        x=0
        while 2**x<=n:
            if 2**x==n:
                return True
            x+=1

        if 2**x==n:
            return True
        else:
            return False
        
# bit manipulation
        return n>0 and n&(n-1)==0