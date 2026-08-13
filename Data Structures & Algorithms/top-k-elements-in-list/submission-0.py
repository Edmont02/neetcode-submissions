class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ref = {}
        for num in nums:
            if num in ref:
                ref[num] += 1
            else:
                ref[num] = 1
        sorted_ref = sorted(ref, key=ref.get, reverse=True)
        return sorted_ref[:k]