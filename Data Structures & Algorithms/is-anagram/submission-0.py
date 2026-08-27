from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Two strings with different lengths cannot be anagrams
        if len(s) != len(t):
            return False
        
        s_letters = defaultdict(int)
        t_letters = defaultdict(int)

        for i in range(len(s)):
            s_letters[s[i]]+=1
            t_letters[t[i]]+=1
        
        return s_letters == t_letters