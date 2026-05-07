class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            #Sort each string and check if there is an anagram of it
            sorted_chars = sorted(s)
            sorted_s = "".join(sorted_chars)
            groups[sorted_s].append(s)
        # print(groups)
        return [l for l in groups.values()]