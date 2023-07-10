"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.
"""


#runtime: 44ms (72% beats), memory: 16.1MB (99.81% beats)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1

        for i in range(len(haystack)):
            if needle == haystack[i:(i+len(needle))]:
                return i