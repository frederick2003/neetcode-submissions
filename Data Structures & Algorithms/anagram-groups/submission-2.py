from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_mapping = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            anagram_mapping[sorted_s].append(s)
        return list(anagram_mapping.values())