class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initialize dictionary
        res = defaultdict(list)
        # for each string in strs
        for s in strs:
            # create array for alphabet letters
            count = [0] * 26
            # for each char in the string
            for c in s:
                # add num times char appears in string to count array
                count[ord(c) - ord('a')] += 1
            # using a tuple with the count array as the key, append the string as it's value
            res[tuple(count)].append(s)
        # return the list of dictionary values
        return list(res.values())