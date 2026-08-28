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
            delim_pos = s.index('#', i)             # Find the next occurance of '#'
            word_length = int(s[i:delim_pos])   # Get encoded word length
            word_start = delim_pos + 1
            word_end = word_start + word_length
            decoded_strings.append(s[word_start:word_end])
            i = word_end
        return decoded_strings