class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            ref = {}
            for i, n in enumerate(nums):
                diff = target - n
                if diff in ref:
                    return [ref[diff], i]
                ref[n] = i