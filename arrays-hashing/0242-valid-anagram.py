   # 242. Valid Anagram
   # https://leetcode.com/problems/valid-anagram/
   # Idea: sorted() arranges both strings alphabetically, so if they are equal, they contain the same letters.
   # Time: O(nlogn)  Space: O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)