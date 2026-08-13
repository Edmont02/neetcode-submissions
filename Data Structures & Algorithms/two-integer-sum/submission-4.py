class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ref = {}
        for i, n in enumerate(nums):
            need = target - n
            if need in ref:
                return [ref[need], i]
            else:
                ref[n] = i