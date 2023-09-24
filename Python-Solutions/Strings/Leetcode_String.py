                                                      #LEETCODE STRING PROBLEMS

#QUESTION NUMBER :: 844. Backspace String Compare  'Easy'
'''-------------------------------------------------------------------------------------------------------------------------------------'''
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process_string(s: str) -> str:
            stack = []
            for char in s:
                if char != '#':
                    stack.append(char)
                elif stack:
                    stack.pop()
            return ''.join(stack)
        
        return process_string(s) == process_string(t)
'''--------------------------------------------------------------------------------------------------------------------------------------'''
#QUESTION NUMBER :: 917. Reverse Only Letters


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        alpha_chars = [ char for char in s if char.isalpha()]
        reversed_chars = []
        for char in s:
            if char.isalpha():
                reversed_chars.append(alpha_chars.pop())
            else:
                reversed_chars.append(char)
        return ''.join(reversed_chars)

'''--------------------------------------------------------------------------------------------------------------------------------------'''

#QUESTION NUMBER : 2810. Faulty Keyboard

class Solution:
    def finalString(self, s: str) -> str:
       rev_str = ""
       for i in range(len(s)):
           if s[i] == "i":
               rev_str = rev_str[:i][::-1]
           else:
               rev_str += s[i]
       return rev_str

'''--------------------------------------------------------------------------------------------------------------------------------------'''

#QUESTION NUMBER : 1185. Day of the Week

from datetime import datetime
import calendar
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        date = ""
        if day < 10:
            date += "0"
        date += str(day) + "/"
        if month < 10:
            date += "0"
        date += str(month) + "/"
        date += str(year) 
        return calendar.day_name[datetime.strptime(date,"%d/%m/%Y").weekday()]

'''--------------------------------------------------------------------------------------------------------------------------------------'''

#QUESTION NUMBER : 2744. Find Maximum Number of String Pairs

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                if words[i]==words[j][::-1]:
                    count += 1

'''--------------------------------------------------------------------------------------------------------------------------------------'''


#QUESTION NUMBER :  1332. Remove Palindromic Subsequences

# Method : 1

class Solution:
    def removePalindromeSub(self, s: str) -> int:
       return 1 if s == s [::-1] else 2

# Method Number: 2
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s: return 0
        l,r = 0,len(s)-1
        while l<r:
            if s[l] != s[r]:
                return 2
            l += 1
            r -= 1
        return 1

'''--------------------------------------------------------------------------------------------------------------------------------------'''

#QUESTION NUMBER : 2788. Split Strings by Separator

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ls = [] 
        for data in words:
            word = data.split(separator)
            for data in word:
                if(data != ""):
                    ls.append(data)
        return ls

'''--------------------------------------------------------------------------------------------------------------------------------------'''