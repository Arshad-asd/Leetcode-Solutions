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

from collections import Counter
from datetime import datetime
import calendar
from itertools import accumulate
import math
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
#QUESTION NUMBER : 2325. Decode the Message
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
       dic = {' ':' '}
       c = 97 
       for i in range(len(key)):
           if key[i] not in dic:
               dic[key[i]] = chr(c)
               c += 1

       result = ''
       for i in range(len(message)):
            result += dic[message[i]]  
       return result

'''--------------------------------------------------------------------------------------------------------------------------------------'''
#QUESTION NUMBER : 2160. Minimum Sum of Four Digit Number After Splitting Digits

class Solution:
    def minimumSum(self, num: int) -> int:
        nums = list(str(num))
        nums.sort()
        return int(nums[0] + nums[-1]) + int(nums[1] + nums[2])


'''--------------------------------------------------------------------------------------------------------------------------------------'''
#QUESTION NUMBER : 1859. Sorting the Sentence
class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        
        sorted_words = sorted(words, key=lambda x: int(''.join(filter(str.isdigit, x))))

        words_without_numbers = [''.join(filter(str.isalpha, word)) for word in sorted_words]

        result = ' '.join(words_without_numbers)

        return result
'''--------------------------------------------------------------------------------------------------------------------------------------'''
#QUESTION NUMBER : 1844. Replace All Digits with Characters
class Solution:
    def replaceDigits(self, s: str) -> str:
        result =''
        for i in range(len(s)):
            if s[i].isnumeric() == True:
                result += chr(ord(s[i-1])+int(s[i]))
            else:
                result +=s[i]
        return result

'''--------------------------------------------------------------------------------------------------------------------------------------'''
#QUESTION NUMBER  : 1812. Determine Color of a Chessboard Square

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        alpha = ['a','b','c','d','e','f','g','h']
        for i in range(len(alpha)):
            for j in range(1,9):
                if alpha[i] + str(j) == coordinates:
                    if (i+j) %  2 == 0:
                        return True
        else:
            return False

'''--------------------------------------------------------------------------------------------------------------------------------------'''
#QUESTION NUMBER  : 1374. Generate a String With Characters That Have Odd Counts

class Solution:
    def generateTheString(self, n: int) -> str:
        return "a" * n if  n % 2 else "a" * (n-1) +"b"


'''--------------------------------------------------------------------------------------------------------------------------------------'''
#QUESTION NUMBER  : 2000. Reverse Prefix of Word
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        reverse = ""
        if ch not in word:
            return word
        for i in range(len(word)):
            if word[i] == ch:
                reverse += word[0:i+1]
                reverse = reverse[::-1]  
                reverse += word[i+1:]
                break
        return reverse

'''--------------------------------------------------------------------------------------------------------------------------------------'''
#QUESTION NUMBER  :1941. Check if All Characters Have Equal Number of Occurrences

#Method 1
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        sets = set()
        for i in range(len(s)):
            count = 0  
            for j in range(len(s)):
                if s[i] == s[j]:
                    count += 1
            sets.add(count)

        return True if len(sets) == 1 else False

#Mehtod 2
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        lst=[]
        for i in s:
            c=s.count(i)
            lst.append(c)
        if min(lst)==max(lst):
            return True
        else:
            return False

#Method 3
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        return len(set(char_count.values())) == 1

'''--------------------------------------------------------------------------------------------------------------------------------------'''
#QUESTION NUMBER  : 1309. Decrypt String from Alphabet to Integer Mapping

#Method 1
class Solution:
    def freqAlphabets(self, s: str) -> str:
        for i in range(26,0,-1):
            s = s.replace(str(i)+"#", chr(ord("a")+i-1)) if i>9 else s.replace(str(i), chr(ord("a")+i-1))
        return s

#Method 2
class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = ""
        i = len(s)-1
        while i>=0:
            if s[i]=="#":
                ans = ans + chr(int(s[i-2:i])+96)
                i=i-2
            else:
                ans = ans + chr(int(s[i])+96)
            i -= 1
        return ans[::-1]
'''--------------------------------------------------------------------------------------------------------------------------------------'''

#QUESTION NUMBER  : 2278. Percentage of Letter in String

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count = s.count(letter)
        percentage = (count / len(s)) * 100
        return math.floor(percentage)

'''--------------------------------------------------------------------------------------------------------------------------------------'''
#QUESTION NUMBER  : 2351. First Letter to Appear Twice
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            if s[i] in res:
                return s[i]
            else:
                res += s[i]
        return res

'''--------------------------------------------------------------------------------------------------------------------------------------'''
#QUESTION NUMBER  : 1684. Count the Number of Consistent Strings

#Method 1
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            if all(char in allowed for char in word):
                count += 1
        return count

#Method 2
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        allow = Counter(allowed)
        for word in words:
            flag = 1
            for letter in word:
                if letter not in allow:
                    flag = 0
                else:
                    continue
            if flag:
                res += 1
        return res
'''--------------------------------------------------------------------------------------------------------------------------------------'''
#QUESTION NUMBER  : 2108. Find First Palindromic String in the Array
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in range(len(words)):
            current_word = words[i]
            if current_word == current_word[::-1]:
                return current_word
        return ""

'''--------------------------------------------------------------------------------------------------------------------------------------'''
#QUESTION NUMBER  : 2185. Counting Words With a Given Prefix

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for i in range(len(words)):
            current_word = words[i]
            if current_word[:len(pref)] == pref:
                count += 1
        return count

'''--------------------------------------------------------------------------------------------------------------------------------------'''
#QUESTION NUMBER :771. Jewels and Stones

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for i in stones:
            if i in jewels:
                count += 1
        return count
'''--------------------------------------------------------------------------------------------------------------------------------------'''
