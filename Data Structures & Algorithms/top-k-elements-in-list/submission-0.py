class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        # Count number frequencies O(n)
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        
        # Add freq counts to a list O(n)
        results = []
        for num, count in counts.items():
            results.append([count, num])
        
        # Sort the list of lists based on the frequency count
        # O(nlogn)
        results.sort()

        top_k = []
        for i in range(k):
            top_k.append(results.pop()[1])
        return top_k

