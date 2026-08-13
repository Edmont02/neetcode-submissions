class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ref = {}
        for i in range(len(nums)):
            need = target - nums[i]

            if need in ref:
                return [ref[need], i]

            ref[nums[i]] = i