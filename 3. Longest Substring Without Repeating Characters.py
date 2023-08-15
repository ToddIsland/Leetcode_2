class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = set()
        res = 0
        l = 0

        for r in range(len(s)):
            while s[r] in store:
                store.remove(s[l])
                l += 1
            store.add(s[r])
            res = max(r - l + 1, res)

        return res
