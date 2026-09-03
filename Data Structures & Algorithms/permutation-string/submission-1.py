class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # Build a char mapping array for two strings
        s1_map, s2_map = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1_map[ord(s1[i]) - ord('a')] += 1
            s2_map[ord(s2[i]) - ord('a')] += 1 
        
        # Use a fixed length sliding window approach.
        # Length of the sliding window is len(s1)
        left = 0
        for right in range(len(s1), len(s2)):
            if s1_map == s2_map:
                return True
            s2_map[ord(s2[left]) - ord('a')] -= 1
            s2_map[ord(s2[right]) - ord('a')] += 1
            left += 1
        return s1_map == s2_map
