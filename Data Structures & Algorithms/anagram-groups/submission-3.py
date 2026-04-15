class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for s in strs:
            sorted_key = "".join(sorted(s))
            if sorted_key not in ans:
                ans[sorted_key] = []
            ans[sorted_key].append(s)
        return list(ans.values())