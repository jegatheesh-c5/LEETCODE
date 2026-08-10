class Solution:
    def myAtoi(self, s):
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        
        sign = 1
        if i < len(s) and s[i] in ['+', '-']:
            if s[i] == '-':
                sign = -1
            i += 1
        
        result = 0
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])

            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 7):
                return INT_MIN if sign == -1 else INT_MAX
            
            result = result * 10 + digit
            i += 1
        
        return sign * result
