"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        i=0
        a=s
        if len(s)%2!=0:
            return False
        else:
            while i <= len(a):
                if "()" in s:
                    s = s.replace("()","")
                if "{}" in s:
                    s = s.replace("{}","")
                if "[]" in s:
                    s = s.replace("[]","")
                if s=="":
                    break

                i+=2


        if s=="":
            return True
        else:
            return False
