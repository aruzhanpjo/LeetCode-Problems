"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        txt = s[::-1]
        new=" "
        for i in txt:
            if i==" " and new==" ":
                continue
            if i!=" ":
                new+=i
            elif i== " " and new!=" ":
                break
        
        ss=new[::-1]
        return len(ss)-1