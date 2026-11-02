class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        right = 0
        seen_chars = set()
        max_length = 0

        while right < len(s):
            if s[right] not in seen_chars:
                seen_chars.add(s[right])
                max_length = max(right - left + 1, max_length)
            else:
                while s[right] in seen_chars:
                    seen_chars.remove(s[left])
                    left += 1
                seen_chars.add(s[right])
            right += 1
                    

        return max_length
        