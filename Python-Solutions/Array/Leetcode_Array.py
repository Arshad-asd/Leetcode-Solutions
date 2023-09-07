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
