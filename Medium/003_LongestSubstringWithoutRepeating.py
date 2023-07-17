"""
Given a string s, find the length of the longest 
substring without repeating characters.
"""


# Runtime: 476 ms, beats - 12.58%, memory 17MB
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        i=0
        j=0
        longest = []
        visited = ""
        theEnd = len(s)-1
        while j<=theEnd:
            if s[j] not in visited:
                visited+=s[j]
                j+=1
            else:
                longest.append(len(visited))
                i+=1
                j=i
                visited=""
                visited+=s[j-1]
                
        longest.append(len(visited))
        if len(longest)>1:
            return max(longest)
        else:
            return longest[0]

            

            