class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        maxf = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])
            # The condition: if window size - most frequent char > replacements allowed
            while (r-l+1) - maxf > k:
                # 1. Decrease the count of the character that is falling out of the window
                count[s[l]] -= 1
                # 2. Shrink the window from the left
                l += 1
            res = max(res, r-l+1)
        return res

        