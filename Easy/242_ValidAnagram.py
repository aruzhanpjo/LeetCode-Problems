"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
"""


# Original solution, runtime 137ms (beats 5.76%), memory 16.9 MB (beats 37.4%)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        for i in s:
            if i in t:
                t = t.replace(i,"",1)

        if t=="":
            return True
        else:
            return False


# New solution with Counter() implementation. Runtime 44ms (beats 98.96%), memory 16.9 MB (beats 964.4%)
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set1 = dict(Counter(s))
        set2 = dict(Counter(t))

        if set1==set2:
            return True
        else:
            return False