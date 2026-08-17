class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        count = 0
        prod = 1

        for n in nums:
            if n == 0:
                count+=1
            if n != 0:
                prod *= n
        
        if count > 1:
            return [0 for i in range(len(nums))]

        if count == 1:
            for n in nums:
                if n == 0:
                    output.append(prod)
                if n != 0:
                    output.append(0)
            return output
        
        if count == 0:
            for n in nums:
                total = prod // n
                output.append(total)
            return output