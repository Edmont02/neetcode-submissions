class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for i in range(len(strs)):
            res.append(str(len(strs[i])))
            res.append("#")
            res.append(strs[i])
        return "".join(res)
            
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
                
            l = int(s[i:j])
            i = j + 1
            j = i + l
            res.append(s[i:j])
            i = j

        return res