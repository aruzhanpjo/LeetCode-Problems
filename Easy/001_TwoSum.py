"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        sum=[]
        while i<len(nums):
            j= i +1
            while j<len(nums): 
                if (nums[i]+nums[j])==target:
                    sum.append(i)
                    sum.append(j)
                    break
                j+=1
            i+=1
        return sum

