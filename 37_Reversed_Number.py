class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self, number):
        # write your code here
       digi1=number//100
       digi2=number//10%10
       digi3=number%10
       
       Reversed=digi3*100+digi2*10+digi1
       
       return Reversed
