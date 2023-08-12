import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = collections.defaultdict(list)

        for s in strs:
            sc = "".join(sorted(s))
            dict[sc].append(s)

        return list(dict.values())
