class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        1. Find the pivot. O(logn)
        2. Select correct subarray.
        3. Perform binary search. 

        nums = [3,4,5,6,1,2]
        target = 1
        """
        # Find the pivot
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        pivot = l

        def binary_search(left: int, right: int) -> int:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        res = binary_search(0, pivot - 1)
        if res != -1:
            return res
        return binary_search(pivot, len(nums) - 1)
        
        
            
        