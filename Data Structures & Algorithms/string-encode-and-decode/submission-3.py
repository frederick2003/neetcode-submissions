class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string = encoded_string + str(len(string)) + '#' + string
        return encoded_string

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        decoded_strings = []
        i = 0
        while i < len(s):
            cur_str_length = ""
            int_checker = i
            while s[int_checker].isdigit():
                cur_str_length = cur_str_length + s[int_checker]
                int_checker+=1
            cur_str_length = int(cur_str_length)
            i = int_checker + 1
            decoded_strings.append(s[i:i+cur_str_length])
            i += cur_str_length
        return decoded_strings