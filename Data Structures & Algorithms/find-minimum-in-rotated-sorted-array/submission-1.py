class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        A binary search question.
        We are not actuallt looking for a minimum we are looking for a
        the point at which the array was rotated.


        Sample
        [3,4,5,6,1,2]
        """
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]