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

# Mehtods 1:

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

# Methods 2:

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = [0] * num_people
        i = 0
        give = 1
        while candies > 0:
                candies_given = min(give, candies)
                result[i] += candies_given
                candies -=  candies_given
                i = (i +1) % num_people
                give +=1
        return result
       
'''--------------------------------------------------------------------------------------------'''

# Question No: 2769. Find the Maximum Achievable Number

class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return  num + 2*t 

'''--------------------------------------------------------------------------------------------'''

# Question No: 2652. Sum Multiples


class Solution:
    def sumOfMultiples(self, n: int) -> int:
        sums = 0
        for i in range(1,n+1):
           if i %3 ==0 or i % 5 == 0 or i % 7 == 0:
                sums = sums + i
        return sums

'''--------------------------------------------------------------------------------------------'''

# Question No: 204. Count Primes
 # setp 1

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        primes = [1] * n
        primes[0] = 0
        primes[1] = 0
        i = 2 
        while i < n:
            temp = i
            if primes[i]:
                temp += i
                while temp < n:
                    primes[temp] = 0
                    temp += i
            i = i + 1
        return sum(primes)

# step 2

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, n, i):
                    is_prime[j] = False

        return sum(is_prime)

'''--------------------------------------------------------------------------------------------'''

# Question No : 2843. Count Symmetric Integers

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def get_digit_sum(num_str):
            return sum(int(digit) for digit in num_str)

        count = 0

        for num in range(low, high + 1):
            num_str = str(num)
            num_len = len(num_str)

            if num_len % 2 == 0:  # Check if it has an even number of digits
                first_half = num_str[:num_len // 2]
                second_half = num_str[num_len // 2:]

                if get_digit_sum(first_half) == get_digit_sum(second_half):
                    count += 1

        return count

'''--------------------------------------------------------------------------------------------'''

# Question No :2469. Convert the Temperature

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15,celsius * 1.80 + 32.00]

'''--------------------------------------------------------------------------------------------'''

# Question No : 2413. Smallest Even Multiple

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n if n % 2 == 0 else n * 2

'''--------------------------------------------------------------------------------------------'''
# Question No : 2894. Divisible and Non-divisible Sums Difference

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = 0
        num2 = 0
        for i in range(1,n+1):
            if i % m == 0:
                num2 += i
            else:
                num1 += i
        return num1 - num2 

'''--------------------------------------------------------------------------------------------'''

# Question No : 2119. A Number After a Double Reversal

#Method : 1
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        def reverse_integer(n):
            return int(str(n)[::-1])

        reversed1 = reverse_integer(num)
        reversed2 = reverse_integer(reversed1)

        return reversed2 == num

#Method : 2
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
         if len(str(num)) > 1 and str(num)[-1] =='0':
             return False
         return True

'''--------------------------------------------------------------------------------------------'''
# Question No : 2427. Number of Common Factors
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        if a > b:
            n = a
        else:
            n = b
        count = 0
        for i in range(1,n+1):
            if a % i == 0 and b % i == 0:
                count += 1
        return count
'''--------------------------------------------------------------------------------------------'''
# Question No : 2169. Count Operations to Obtain Zero
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        while num1 > 0 and num2 > 0:
            if num1 >= num2:
                num1 = num1 - num2
            else:
                num2 = num2 - num1
            count += 1
        return count
'''--------------------------------------------------------------------------------------------'''
# Question No : 2396. Strictly Palindromic Number
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        b = bin(n)
        if b == b[::-1]:
           return True
        return False

'''--------------------------------------------------------------------------------------------'''

# Question No : 2220. Minimum Bit Flips to Convert Number

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start_bin = bin(start)[2:]
        goal_bin = bin(goal)[2:]
        flips = 0

        len_diff = abs(len(start_bin) - len(goal_bin))

        if len(start_bin) < len(goal_bin):
            start_bin = '0' * len_diff + start_bin
        else:
            goal_bin = '0' * len_diff + goal_bin

        for i in range(len(start_bin)):
            if start_bin[i] != goal_bin[i]:
                flips += 1
                start_bin = start_bin[:i] + goal_bin[i] + start_bin[i + 1:]

        return flips


'''--------------------------------------------------------------------------------------------'''
# Question No : 2562. Find the Array Concatenation Value
class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        res = 0

        while nums:
            concat = str(nums.pop(0))

            if nums:
                concat += str(nums.pop())

            res += int(concat)

        return res

'''--------------------------------------------------------------------------------------------'''
#QUESTION NUMBER  : 2042. Check if Numbers Are Ascending in a Sentence
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        numbers = [int(match.group()) for match in re.finditer(r'\b\d+\b', s)]

        for i in range(len(numbers)-1):
            if numbers[i] >= numbers[i+1]:
                return False

        return True