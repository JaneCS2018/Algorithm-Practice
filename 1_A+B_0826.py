class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b 
    """
    def aplusb(self, a, b):
        # write your code here
        a = self.int32(a)
        b = self.int32(b)
        return (a^b)+((a & b)<<1)
        
    def int32(self, a):
        import ctypes
        return ctypes.c_int32(a).value
    
