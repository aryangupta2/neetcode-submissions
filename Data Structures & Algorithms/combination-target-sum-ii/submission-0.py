class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        candidates.sort()

        def backtrack(start, path, sum):
            if sum > target:
                return
            if sum == target:
                result.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, path, sum + candidates[i])
                path.pop()

        backtrack(0, [], 0)
        return result
        