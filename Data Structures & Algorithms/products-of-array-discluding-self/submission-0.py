class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Build a prefix sum array 
        prefix = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        # Build a postfix array
        postfix = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]

        # Build the product array
        result = []
        for i in range(len(nums)):
            result.append(prefix[i] * postfix[i])
        return result