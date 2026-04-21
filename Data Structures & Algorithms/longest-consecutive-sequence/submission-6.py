class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest_streak = 0

        for num in hashset:
            # 1. เช็คว่าเป็นจุดเริ่มหรือไม่ (ต้องไม่มีตัวก่อนหน้า)
            if num - 1 not in hashset:
                current_num = num
                current_streak = 1

                # 2. ไหลต่อไปข้างหน้าจนกว่าจะสุดสาย
                while current_num + 1 in hashset:
                    current_num += 1
                    current_streak += 1

                # 3. อัปเดตค่าที่ยาวที่สุดที่เคยเจอ
                longest_streak = max(longest_streak, current_streak)

        return longest_streak