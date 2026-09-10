from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left , right = 1, max(piles)
        min_k = right
        while left <= right:
            current_k = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += ceil(pile/current_k)
            if hours <= h:
                min_k = current_k
                right = current_k - 1
            else:
                left = current_k + 1
        return min_k