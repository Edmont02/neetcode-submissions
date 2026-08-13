class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ref = {}
        for i, j in enumerate(strs):
            sorted_str = "".join(sorted(j))
            if sorted_str in ref:
                ref[sorted_str].append(j)
            else:
                ref[sorted_str] = [j]

        return list(ref.values())