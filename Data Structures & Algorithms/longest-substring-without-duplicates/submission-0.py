"""
1. the while loop keep shrinking from the left
until the character you have just added s[right] is no longer duplicate
while state[s[right]] > 1:
    state[s[left]] -= 1
    left += 1
result = max(result, right-left+1)
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        result = 0
        state = {}

        for right in range(len(s)):
            state[s[right]] = state.get(s[right], 0) + 1

            while state[s[right]] > 1:
                state[s[left]] -= 1
                left += 1
            result = max(result, right-left+1)
        return result
        