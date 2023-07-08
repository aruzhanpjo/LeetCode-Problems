"""
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
"""

class Solution:
    def reverse(self, x: int) -> int:
        num=""
        theStr=str(x)[::-1]
        if theStr[-1]=="-":
            num+="-"
            theStr = theStr.replace("-","")
        
        
        for i in theStr:
            if i=="0":
                theStr.replace("0","")
            else:
                break
        

        num+=theStr

        #adding the restrictions
        if int(num)<-2**31 or int(num)>2**31-1:
            return 0


        return int(num)

            


            

