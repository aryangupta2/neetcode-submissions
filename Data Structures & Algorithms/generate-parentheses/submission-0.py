class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []

        def backtrack(path, opening, closing):
            
            if len(path) == n * 2:
                if opening == closing:
                    result.append(path[:])
                    return
                else:
                    return
            
            # take (
            if opening < n:
                path += '('
                backtrack(path, opening + 1, closing)
                path = path[:-1]

            # take )
            if closing < opening:
                path += ')'
                backtrack(path, opening, closing + 1)
                path = path[:-1]
        
        backtrack("", 0, 0)
        return result
        