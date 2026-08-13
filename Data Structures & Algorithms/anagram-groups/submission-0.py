class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs is None:
            return [strs]
        if len(strs) == 0:
            return []
        
        ref = {}
        arr = []

        for i, n in enumerate(strs):
            key = "".join(sorted(n))
            if key in ref:
                loc = ref[key]
                arr[loc].append(n)
            else:
                ref[key] = len(arr)
                arr.append([n])
            
        return arr