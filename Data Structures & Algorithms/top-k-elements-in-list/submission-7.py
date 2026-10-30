class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if k == len(nums):
            return nums

        counts = {}
        freqs = [[] for _ in range(len(nums))]
        result = []

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        for key, value in counts.items():
            freqs[value - 1].append(key)

        i = len(freqs) - 1
        
        while k > 0 and i >= 0:
            if freqs[i]:
                for num in freqs[i]:
                    result.append(num)
                    k -= 1
            i -= 1

        return result
            
        