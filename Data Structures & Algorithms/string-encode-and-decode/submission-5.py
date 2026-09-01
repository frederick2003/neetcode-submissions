class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += str(len(string)) + '#' + string
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        i = 0
        while i < len(s):
            delimiter_pos = s.index('#', i)
            length = int(s[i:delimiter_pos])
            start = delimiter_pos + 1
            decoded_strings.append(s[start:start + length])
            i = start + length
        return decoded_strings