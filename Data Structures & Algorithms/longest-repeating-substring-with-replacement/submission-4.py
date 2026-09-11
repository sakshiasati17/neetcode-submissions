class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_l = 0
        left = 0
        freq = {}

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1

            max_val = max(freq.values())

            replace = (right - left + 1) - max_val

            while replace > k:
                freq[s[left]] -= 1
                left+=1
                max_val = max(freq.values())
                replace = (right - left + 1) - max_val
            max_l = max(max_l, right - left + 1)
        return max_l