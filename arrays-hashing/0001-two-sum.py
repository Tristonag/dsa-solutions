# 1. Two Sum
# https://leetcode.com/problems/two-sum/
# Idea: Check every pair of numbers to find two that add up to the target.
# Time: O(n^2)  Space: O(1)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]