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
from itertools import accumulate
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

#QUESTION NUMBER :      2710. Remove Trailing Zeros From a String

class Solution:
    def removeTrailingZeros(self, num: str) -> str:
       while(num[-1] == '0'):
           num = num[:-1]
       return num

'''--------------------------------------------------------------------------------------------------------------------------------------'''
#QUESTION NUMBER : 1021. Remove Outermost Parentheses

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        count = 0
        for i in s :
            if i == '(' and count > 0:
                res.append(i)
            if i == ')' and count > 1:
                res.append(i)
            count += 1 if i == '(' else -1
        return "".join(res)

'''--------------------------------------------------------------------------------------------------------------------------------------'''

#QUESTION NUMBER : 1678. Goal Parser Interpretation

class Solution:
    def interpret(self, command: str) -> str:
         command = command.replace("()","o")
         command = command.replace("(al)", "al")
         return command
'''--------------------------------------------------------------------------------------------------------------------------------------'''
#QUESTION NUMBER : 1528. Shuffle String

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = ''
        for i in range(len(indices)):
           res += s[indices.index(i)]
        return res

'''--------------------------------------------------------------------------------------------------------------------------------------'''
#QUESTION NUMBER : 1221. Split a String in Balanced Strings
class Solution:
    def balancedStringSplit(self, s: str) -> int:
       return list(accumulate(1 if c =='R' else -1 for c in s)).count(0)
'''--------------------------------------------------------------------------------------------------------------------------------------'''
#QUESTION NUMBER : 1592. Rearrange Spaces Between Words

class Solution:
    def reorderSpaces(self, text: str) -> str:
        space = text.count(" ")
        words = text.split()
        wordlen = len(words)
        if wordlen-1>0:
            c = space//(wordlen-1)
        else:
            c = space
        res = ""
        for i in words:
            res += i
            if space >= c:
                res += " "*c
                space -= c

        if space>0:
            res += " "*space
        return res

'''--------------------------------------------------------------------------------------------------------------------------------------'''