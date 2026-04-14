class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                index_of_complement = seen[complement]

                return [index_of_complement, i]
            seen[num] = i