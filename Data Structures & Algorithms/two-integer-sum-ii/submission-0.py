"""
           * *
numbers = [1,2,3,4], target = 3
1 + 4 = 5 > target
move right pointer to the left
1 + 3 = 4 > target 
move to left
1 + 2 = 3 == target
return [numbers[l],numbers[r]]


take note:
r = len(numbers)-1
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1

        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l+1, r+1]
            elif total > target:
                r -= 1
            else:
                l += 1
        