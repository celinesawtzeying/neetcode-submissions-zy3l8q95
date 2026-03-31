from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)

        for num in nums:
            res[num] += 1
        items = res.items()
        sorted_items = sorted(items, key=lambda x:x[1],reverse = True)[:k]
        return [item[0] for item in sorted_items]

