class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        result = []
        nums.sort()

        def backtrack(index, path):
            
            if index == len(nums):
                result.append(path[:])
                return
            
            # take the path
            path.append(nums[index])
            backtrack(index + 1, path)
            path.pop()

            # dont take the path
            curr = nums[index]
            while index < len(nums) and nums[index] == curr:
                index += 1
            backtrack(index, path)

        backtrack(0, [])
        return result
            

            
            
        