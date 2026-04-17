class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [1] * n
        
        # 1. วิ่งไปข้างหน้า (เก็บผลคูณฝั่งซ้าย)
        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]
            
        # 2. วิ่งถอยหลัง (คูณด้วยผลคูณฝั่งขวา)
        suffix = 1
        for i in range(n - 1, -1, -1): # เริ่มจากตัวสุดท้าย ถอยมาถึงตัวแรก
            ans[i] *= suffix
            suffix *= nums[i]
            
        return ans