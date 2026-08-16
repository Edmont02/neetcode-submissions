class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ref = {}
        for n in nums:
            if n in ref:
                ref[n] += 1
            else:
                ref[n] = 1
        sorted_ref = sorted(ref, key=ref.get, reverse=True)
        return sorted_ref[:k]