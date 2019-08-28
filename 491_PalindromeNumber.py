class Solution:
    """
    @param num: a positive number
    @return: true if it's a palindrome or false
    """
    def isPalindrome(self, num):
        # write your code here
        reversed = 0
        a = abs(num)
        
        while(a!=0):
            tmp=a%10
            reversed=reversed*10 + tmp
            a = a//10
            
        if a>=0 and reversed==num:
            return True
        else:
            return False
        
