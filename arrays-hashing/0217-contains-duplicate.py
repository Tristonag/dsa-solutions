# 217. Contains Duplicate (Easy)
# https://leetcode.com/problems/contains-duplicate/
# Idea: set() keeps only unique values, so if the set is shorter than the list, something was duplicated.
# Time: O(n)  Space: O(n)

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(nums) > len(set(nums)):
            return True
        else:
            return False