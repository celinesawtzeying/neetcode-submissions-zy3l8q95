class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = [0] * 26
        win_count = [0] * 26
        left = 0

        for c in s1:
            s1_count[ord(c) - ord('a')] += 1
        
        for right in range(len(s2)):
            win_count[ord(s2[right]) - ord('a')] += 1
        
            if right - left + 1 > len(s1):
                win_count[ord(s2[left]) - ord('a')] -= 1
                left += 1
            
            if s1_count == win_count:
                return True
        return False
        