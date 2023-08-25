                                                            #LEETCODE ARAY QUESTIONS SOLVED

# QUESTIOIN NO : 9. Palindrome Number

'''--------------------------------------------------------------------------------------------'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        num, temp = 0, x
        
        while temp != 0:
            num = num * 10 + temp % 10
            temp //= 10
        
        return num == x

'''--------------------------------------------------------------------------------------------'''
