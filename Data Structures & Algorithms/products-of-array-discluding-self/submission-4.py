class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        len_nums = len(nums)

        left_product = 1
        left_products = []

        for i in range(len_nums):
            left_products.append(left_product)
            left_product *= nums[i]
        
        right_product = 1
        right_products = []

        for i in range(len_nums - 1, -1, -1):
            right_products.append(right_product)
            right_product *= nums[i]

        right_products.reverse()

        result = []
        for i in range(len_nums):
            result.append(left_products[i] * right_products[i])

        return result
            
            
        