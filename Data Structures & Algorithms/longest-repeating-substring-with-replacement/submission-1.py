class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        occurrences = {}
        longest_substring = 0
        left = 0

        for right in range(len(s)):
            occurrences[s[right]] = occurrences.get(s[right], 0) + 1
            if (right - left + 1) - max(occurrences.values()) > k:
                while (right - left + 1) - max(occurrences.values()) > k:
                    occurrences[s[left]] -= 1
                    left += 1
                    if occurrences[s[left]] == 0:
                        del occurrences[s[left]]
            else:
                longest_substring = max(longest_substring, right - left + 1)

        return longest_substring
        