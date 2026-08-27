class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        element_set = set()
        for num in nums:
            if num in element_set:
                return True
            element_set.add(num)

        return False

        