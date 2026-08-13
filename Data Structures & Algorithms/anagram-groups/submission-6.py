class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ref = {}
        for s in strs:
            sorted_str = "".join(sorted(s))
            if sorted_str in ref:
                ref[sorted_str].append(s)
            else:
                ref[sorted_str] = [s]

        return list(ref.values())