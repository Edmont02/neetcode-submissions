class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sorted_n = sorted(nums)
        longest = 1
        current = 1

        for i in range(1, len(sorted_n)):
            if sorted_n[i] != sorted_n[i-1]:
                if sorted_n[i] == sorted_n[i-1] + 1:
                    current +=1
                else:
                    longest = max(longest, current)
                    current = 1
            
        return max(longest, current)