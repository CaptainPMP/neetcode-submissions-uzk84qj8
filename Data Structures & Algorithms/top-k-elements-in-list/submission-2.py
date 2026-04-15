class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = {}
        for num in nums:
            ans[num] = ans.get(num, 0) + 1
        ans = dict(sorted(ans.items(), reverse=True, key=lambda item: item[1]))
        # print(list(ans.keys())[:k])
        return list(ans.keys())[:k]