                                            #LEETCODE ARAY QUESTIONS SOLVED

'''--------------------------------------------------------------------------------------------'''

# QUESTIOIN NO : 896. Monotonic Array

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = decreasing = True
        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                increasing = False
            if nums[i] < nums[i + 1]:
                decreasing = False
        
        return increasing or decreasing

'''--------------------------------------------------------------------------------------------'''

# QUESTION NO: 1. Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []

'''--------------------------------------------------------------------------------------------'''
# QUESTION NO: 961. N-Repeated Element in Size 2N Array

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        count_map = {}
        n = len(nums)
        target_count = n // 2
        
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1
            if count_map[num] == target_count:
                return num


'''--------------------------------------------------------------------------------------------'''

# QUESTION NO: 1128. Number of Equivalent Domino Pairs

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        domino_counts = {}
        total_pairs = 0
        for domino in dominoes:
            domino.sort()
            identifier = tuple(domino)
            domino_counts[identifier] = domino_counts.get(identifier,0) + 1
        for count in domino_counts.values():
            total_pairs += (count * (count -1)) // 2
        return total_pairs

'''--------------------------------------------------------------------------------------------'''


# QUESTION NO: 27. Remove Element

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0 
        j = 0

        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i +=1
            j +=1
        return i
'''--------------------------------------------------------------------------------------------'''

# QUESTION NO: 118. Pascal's Triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            lists = [[1],[1,1]]
            for i in range(2,numRows):
                temp = []
                for j in range(0,i+1):
                      if j==0 or j==i:
                        temp.append(1)
                      else:
                        temp.append(lists[i-1][j-1]+lists[i-1][j])
                lists.append(temp)
            return lists

'''--------------------------------------------------------------------------------------------'''

# QUESTION NO: 2215. Find the Difference of Two Arrays

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1Set, nums2Set = set(nums1) , set(nums2)
        res1, res2 = set(), set()

        for n in nums1:
            if n not in nums2Set:
                res1.add(n)
        
        for n in nums2:
            if n not in nums1Set:
                res2.add(n)

        return [list(res1), list(res2)]

'''--------------------------------------------------------------------------------------------'''

# QUESTION NO : 2824. Count Pairs Whose Sum is Less than Target

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
               if nums[i] + nums[j] < target:
                   count += 1
        return count

'''--------------------------------------------------------------------------------------------'''

# QUESTION NO : 1200. Minimum Absolute Difference

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
       arr.sort()
       min_dif = float('inf')
       res = []
       for i in range(1 ,len(arr)):
           cur = abs(arr[i] - arr[i -1])
           if min_dif > cur:
               min_dif = cur
               res = [[arr[i-1], arr[i]]]
           elif min_dif == cur:
               res.append([arr[i-1],arr[i]])
       return res
'''--------------------------------------------------------------------------------------------'''
