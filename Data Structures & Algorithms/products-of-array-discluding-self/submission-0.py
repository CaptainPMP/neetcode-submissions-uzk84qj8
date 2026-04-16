class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):

            sum = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                sum *= nums[j]
            ans.append(sum)
                
        return ans