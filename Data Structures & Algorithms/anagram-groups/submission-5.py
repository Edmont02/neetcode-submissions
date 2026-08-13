class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ref = {}
        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted_str in ref:
                ref[sorted_str].append(str)
            else:
                ref[sorted_str] = [str]

        return list(ref.values())