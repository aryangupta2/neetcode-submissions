class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        len_nums = len(nums)

        left_product = 1
        products = []

        for i in range(len_nums):
            products.append(left_product)
            left_product *= nums[i]
        
        right_product = 1

        for i in range(len_nums - 1, -1, -1):
            products[i] *= right_product
            right_product *= nums[i]

        return products
            
            
        