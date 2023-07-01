class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor==-1 and dividend<-1:
            return (dividend*(-1))-1
        a=dividend/divisor
        return int(a)
    