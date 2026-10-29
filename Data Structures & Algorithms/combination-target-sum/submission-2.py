class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, path, sum):
            
            if sum > target:
                sum = 0
                return

            if sum == target:
                sum = 0
                result.append(path[:])
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, path, sum + nums[i])
                path.pop()

        backtrack(0, [], 0)
        return result