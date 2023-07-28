"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

# Dynamic Programming
# runtime - 33ms, 98.29% beats, memory 16.2MB, 92,74% beats



class Solution: 
    def climbStairs(self, n: int) -> int:
        temp = 0
        pre = 1
        curr = 1

        for i in range(1, n):
            temp = curr
            # counting the previous steps we used to get to the current point
            curr = curr+pre
            pre = temp

        return curr