class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_len = len(nums)
        nums = set(nums)
        l = len(nums)

        if nums_len > l:
            return True
        else:
            return False