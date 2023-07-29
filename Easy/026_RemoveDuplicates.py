"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""



#brute force + didn't fully understand the question
# runtime - 156ms, 16.67% beats, memory - 17.91MB, 58.35% beats

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #create a list ofthe unique elements
        theSorted = []

        i=0
        while i <len(nums):
            #keep the same index, as we get rid of 1 element; 
            #hence, the size will decrease by 1 & we are alreadt "moving" through the list
            if nums[i] in theSorted:
                nums.pop(i)
            
            #otherwise add to the list of unique elements
            else:
                theSorted.append(nums)
                i+=1
                

        k = len(nums)
        return k
    


    # optimized the solution + learned new python methods
    # runtime - 80ms, beats 99.64%, memory - 18.04MB, beats 15,94%
    class Solution:
        def removeDuplicates(self, nums: List[int]) -> int:
            # nums[:] basically means a shallow copy of nums
            # sorted is a function that returns a sorted list, while .sort() is a method that sorts the list in place
            nums[:] = list(sorted(set(nums)))
            return len(nums)