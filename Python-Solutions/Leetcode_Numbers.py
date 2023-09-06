                                                            #LEETCODE ARAY QUESTIONS SOLVED

'''--------------------------------------------------------------------------------------------'''

# QUESTIOIN NO : 9. Palindrome Number

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

# QUESTIOIN NO : 326. Power of Three

#Mehthods 1:

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n //=3
        return n==1

#Mehthods 2:

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        power = int(round(math.log(n,3)))
        return 3**power == n
    
'''--------------------------------------------------------------------------------------------'''

# 1103. Distribute Candies to People

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        arr = [ 0 for i in range(num_people)]
        i = 0
        j = 1
        while candies > 0:
            if i == len(arr):
                i = 0
            if candies >= j:
                arr[i] += j
                candies -= j
                j += 1
            else:
                arr[i] += candies
                break
            i += 1
        return arr

'''--------------------------------------------------------------------------------------------'''