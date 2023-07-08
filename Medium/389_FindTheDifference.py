"""

"""
from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        set1 = Counter(s)
        set2 = Counter(t)

        set1.subtract(set2)

        #looking for a value that is not in s 
        for i in set1:
            if set1[i]!=0:
                return i