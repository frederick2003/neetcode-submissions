class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Essentially a next greater element question.
        Use a monotonic decreasing stack.
        Pop elements when the current element is greater than the stack top.
        """
        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                last_colder_day_index = stack.pop()
                result[last_colder_day_index] = i - last_colder_day_index
            stack.append(i)
        return result

