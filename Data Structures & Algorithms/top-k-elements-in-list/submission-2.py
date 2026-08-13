class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ref = {}
        for n in nums:
            if n in ref:
                ref[n] += 1
            else:
                ref[n] = 1
                
        result = dict(sorted(ref.items(), key=lambda item: item[1], reverse=True))
        k_keys = list(result.keys())[:k]
        return k_keys