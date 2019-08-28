"""
Max of 3 numbers
"""
def maxOfThreeNumbers(self, num1, num2, num3):
        # write your code here
        arr=[num1, num2, num3]
        arr.sort(reverse=True)
        return arr[0]
