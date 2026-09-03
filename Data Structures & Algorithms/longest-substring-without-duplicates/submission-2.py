class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        longest_length = 0
        for right in range(len(s)):
            current_char = s[right]
            while current_char in seen:
                seen.remove(s[left])
                left += 1
            seen.add(current_char)
            longest_length = max(longest_length, (right - left) + 1)
                
        return longest_length