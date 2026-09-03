class Solution:
    def isValid(self, s: str) -> bool:
        close_bracket_mapping = {")":"(","}":"{","]":"["}
        stack = []
        for cur_b in s:
            if cur_b in close_bracket_mapping:
                if stack and close_bracket_mapping[cur_b] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(cur_b)
        return len(stack) == 0