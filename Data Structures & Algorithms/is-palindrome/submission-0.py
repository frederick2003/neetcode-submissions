class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Build a new string with whitespace and non-alphanumeric chars stripped.
        stripped_string = ""
        for char in s.strip():
            if char.isalnum():
                stripped_string += char.lower()
        l = 0
        r = len(stripped_string) - 1
        while l < r:
            if stripped_string[l] != stripped_string[r]:
                return False
            l += 1
            r -= 1
        return True