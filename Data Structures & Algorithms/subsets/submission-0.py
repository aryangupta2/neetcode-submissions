class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
         
        def backtrack(index, path):
            if index == len(nums):
                result.append(path[:])
                return
            
            # take the path
            path.append(nums[index])
            backtrack(index + 1, path)
            path.pop()

            # dont take the path
            backtrack(index + 1, path)
            
        backtrack(0, [])
        return result
