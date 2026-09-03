class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        longest_length = 0
        for right in range(len(s)):
            current_char = s[right]

            # If the current character is not a duplicate, add to set
            if current_char not in seen:
                seen.add(current_char)
            # If the current character is a duplicate, calculate length and
            # keep removing elements from the set until the character is 
            # no longer in the set.
            else:
                longest_length = max(longest_length, len(seen))
                while current_char in seen:
                    seen.remove(s[left])
                    left += 1
                seen.add(current_char)
        return max(longest_length, len(seen))