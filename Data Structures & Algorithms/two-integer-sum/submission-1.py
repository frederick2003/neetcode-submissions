class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        index_target_mapping = {}

        for i, num in enumerate(nums):
            delta = target - num
            if delta in index_target_mapping:
                return [index_target_mapping[delta], i]
            index_target_mapping[num] = i