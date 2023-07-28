"""
Given a string s, return the longest palindromic substring in s.
"""

#code solution & explanation from neetcode.
#need to revise!

#runtime - 482ms, 90.39% beats, memory - 16.46MB, 47.62% beats


#algorithm is to compare the left & right sides from a center point & see if they are the same.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        theResult = ""
        maxLen = 0

        for i in range(len(s)):
            # odd legth
            l, r = i, i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>maxLen:
                    theResult = s[l:r+1]
                    maxLen = r-l+1
                r+=1
                l-=1

            #even length
            l,r = i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>maxLen:
                    theResult = s[l:r+1]
                    maxLen = r-l+1
                r+=1
                l-=1      

        return theResult