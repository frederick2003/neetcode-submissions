class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        NOTES
        ------------------------------------------------------------

        1. Can only make k replacements.
        2. Can replace k elements with any other uppercase char.
        3. Replace the k elements with the most frequent char
        """
        count = [0] * 26
        left = 0
        maximum = 0
        for right in range(len(s)):
            count[ord(s[right].lower()) - ord('a')] += 1
            while (right - left + 1) - max(count) > k:
                count[ord(s[left].lower()) - ord('a')] -= 1
                left += 1
            maximum = max(maximum, right - left + 1)
        return maximum
