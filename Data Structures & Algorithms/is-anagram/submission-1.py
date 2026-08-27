from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Two strings with different lengths cannot be anagrams
        if len(s) != len(t):
            return False
        
        # Initialise two character counts for the two string
        s_letters = defaultdict(int)
        t_letters = defaultdict(int)

        # Build a character mapping for the two strings
        for i in range(len(s)):
            s_letters[s[i]]+=1
            t_letters[t[i]]+=1
        
        # If char mappings are the same then True else False
        return s_letters == t_letters