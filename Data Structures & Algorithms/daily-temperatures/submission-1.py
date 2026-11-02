class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        temp_stack = [0]
        result = [0] * len(temperatures)

        for i in range(1, len(temperatures)):
            while len(temp_stack) > 0 and temperatures[temp_stack[-1]] < temperatures[i]:
                popped_index = temp_stack.pop()
                result[popped_index] = i - popped_index
            temp_stack.append(i)
        
        return result



        
            
        