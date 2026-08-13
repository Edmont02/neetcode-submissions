class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ref = {}
        for val in strs:
            key = "".join(sorted(val))
            if key in ref:
                ref[key].append(val)
            else:
                ref[key] = [val]
        return list(ref.values())