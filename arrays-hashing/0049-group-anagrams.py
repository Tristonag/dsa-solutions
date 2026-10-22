# 49. Group Anagrams
## https://leetcode.com/problems/group-anagrams/
# Idea: Sort each word's letters and use the sorted word as a dictionary key to group anagrams.
# Time: O(n * k log k)  Space: O(n * k)

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}

        for word in strs:
            key = ''.join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())