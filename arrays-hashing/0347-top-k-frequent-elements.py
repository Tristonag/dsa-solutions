# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/
# Idea: Use a dictionary to count each number, then sort the numbers by frequency and return the first k.
# Time: O(n + m log m)  Space: O(m)

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        sorted_nums = sorted(freq, key=freq.get, reverse=True)

        return sorted_nums[:k]
