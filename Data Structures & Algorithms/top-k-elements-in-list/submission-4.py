class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Build a character count O(n)
        element_counts = {}
        for num in nums:
            element_counts[num] = 1 + element_counts.get(num, 0)
        
        # Add the num counts to an array
        mapping = [[]*len(nums) for _ in range(len(nums) + 1)]
        for num, count in element_counts.items():
            mapping[count].append(num)
        
        # Iterate backwards through the mapping list grabbing the top k elements
        result = []
        for i in range(len(mapping) - 1, 0, -1):
            for num in mapping[i]:
                result.append(num)
                if len(result) == k:
                    return result
