"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word=""

        if len(strs)==1:
            for i in strs:
                word+=i

            return word
        

        strs.sort()

        #check if the first two words have a common prefix
        for x in range(len(strs[0])):
            if strs[0][x]!=strs[1][x]:
                break
            else:
                word+=strs[0][x]

        #if common prefix doesn't match the last word, remove the last letter and try again
        while word not in strs[-1]:
            word = word[:-1]
        
        #if neither match, return empty string
        if word!="" and strs[-1][0]!=word[0]:
            return ""
        else:
            return word
