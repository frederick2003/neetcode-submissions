class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert the list to a set for O(1) lookups
        nums_set = set(nums)

        # Begin a list of numbers where num - 1 is not in the set. 
        # These numbers are the beginning of the sequence.
        starting_sequence_numbers = []
        for num in nums:
            if num - 1 not in nums_set:
                starting_sequence_numbers.append(num)
        
        # Find the longest consecutive sequence length
        longest_sequence_length = 0
        for starting_number in starting_sequence_numbers:
            cur_sequence_length = 1
            next_number = starting_number + 1
            while next_number in nums_set:
                cur_sequence_length += 1
                next_number += 1
            longest_sequence_length = max(longest_sequence_length, cur_sequence_length)
        
        return longest_sequence_length