class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for s in strs:
            counted_key = "".join(sorted(s))
            if counted_key not in ans:
                ans[counted_key] = []
            ans[counted_key].append(s)
        return list(ans.values())