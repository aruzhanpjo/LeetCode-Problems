'''A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.'''

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=re.sub("[^A-Za-z0-9]","",s)
        theInv=a.lower()[::-1]
        if theInv==a.lower():
            return True
        else:
            return False

