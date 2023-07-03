"""
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, 
return the number of negative numbers in grid.
"""

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        sum=0
        # iterate through the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]<0:
                    sum+=1


        return sum