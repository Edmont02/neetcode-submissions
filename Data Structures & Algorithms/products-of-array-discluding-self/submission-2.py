class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prod = 1
        count = 0

        for n in nums:
            if n != 0:
                prod *= n
            if n == 0:
                count += 1

        if count > 1:
            return [0 for i in range(len(nums))]

        res = []
        if count == 1:
            for n in nums:
                if n == 0:
                    res.append(prod)
                else:
                    res.append(0)
            return res

        for n in nums:      
            total = prod // n
            res.append(total)
        return res