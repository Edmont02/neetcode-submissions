class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs is None:
            return [strs]
        if len(strs) == 0:
            return []
        
        ref = {}
        arr = []

        for s in strs:
            key = "".join(sorted(s))
            if key in ref:
                loc = ref[key]
                arr[loc].append(s)
            else:
                ref[key] = len(arr)
                arr.append([s])
            
        return arr