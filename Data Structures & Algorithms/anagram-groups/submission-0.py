class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freqs = {}

        for s in strs:
            counts = {}
            for char in s:
                counts[char] = counts.get(char, 0) + 1
            
            counts_arr = []
            for key, value in counts.items():
                counts_arr.append((key, value))

            counts_arr.sort()

            counts_arr = tuple(counts_arr)

            if counts_arr not in freqs:
                freqs[counts_arr] = []

            freqs[counts_arr].append(s)
            
        return list(freqs.values())

        