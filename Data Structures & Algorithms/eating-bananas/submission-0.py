import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def count_total_hours(k):
            total_hours = 0
            for i in range(len(piles)):
                total_hours += math.ceil(piles[i] / k)
            return total_hours

        lo, hi = 1, max(piles) + 1 # search space

        while lo < hi:
            mid = (lo + hi) // 2
            if count_total_hours(mid) > h:   # condition
                lo = mid + 1
            else:
                hi = mid
        
        return lo
        # return the first element that is count_total_hours(mid) <= h