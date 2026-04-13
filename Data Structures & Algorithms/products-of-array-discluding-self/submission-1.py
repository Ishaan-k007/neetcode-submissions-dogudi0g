class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        results = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if j == i:
                    pass
                else:
                    product = product * nums[j]
            results.append(product)
        return results

        
        