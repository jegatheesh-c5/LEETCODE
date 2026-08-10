class Solution:
    def reverse(self, x):
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        result = 0
        num = abs(x)
        
        while num != 0:
            digit = num % 10
            num //= 10
            
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 7):
                return 0
            
            result = result * 10 + digit
        
        return -result if x < 0 else result
