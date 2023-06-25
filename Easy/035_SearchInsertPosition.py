'''Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)

        val=True
        while val:
            for i in nums:
                if target<i:
                    return nums.index(i)
                    val=False
                        
            else:
                return len(nums)
                val=False