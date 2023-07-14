"""
Given an integer array nums, return true if any value 
appears at least twice in the array, and return false if every element is distinct.
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # could not solve; learned about set().
        
        numSet=set()

        for i in nums:
            if i in numSet:
                return True
            else:
                numSet.add(i)
        
        return False