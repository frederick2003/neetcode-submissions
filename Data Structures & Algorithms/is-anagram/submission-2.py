class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(1) space complexity solution, well actuall O(26) -> O(1)
        # constant time.

        # If different lengths, can never be anagrams
        if len(s) != len(t):
            return False
        
        char_counts = [0] * 26
        for i in range(len(s)):
            char_counts[ord(s[i]) - ord('a')] += 1
            char_counts[ord(t[i]) - ord('a')] -= 1
        
        for count in char_counts:
            if count != 0:
                return False

        return True

        