"""
PROBLEM: 1. Two Sum
PATTERN: Arrays & Hashing (One-Pass Hash Map)
DIFFICULTY: 🟢 Easy

-------------------------------------------------------------------------------
THE "AHA!" MOMENT:
Instead of looking for two numbers that add up to a target (which is O(n^2)), 
we look for the "Complement" (target - current_number). By storing every 
number we've seen in a Hash Map, we can check if the complement exists in O(1).
-------------------------------------------------------------------------------

REVISION LOG:
- Optimization: Use a "One-Pass" approach. We can build the hash map while 
  simultaneously checking for the complement.
- Constraint: The problem guarantees exactly one solution, so we don't need 
  to handle cases with multiple pairs or no solution.
-------------------------------------------------------------------------------
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      complement = {}
      for i in range(len(nums)):
        diff = target - nums[i]
        if diff in complement:
          return [complement[diff], i]
        complement[nums[i]] = i
            
"""
    COMPLEXITY ANALYSIS:
    
    Time Complexity: O(n)
    - We iterate through the list of 'n' elements exactly once.
    - Each dictionary lookup and insertion is O(1) on average.

    Space Complexity: O(n)
    - In the worst case, we store 'n' elements in the hash map before 
      finding the complement (if it's at the very end of the list).
    """

# --- INTERVIEW TALKING POINTS ---
# 1. "I used a One-Pass Hash Map approach to reduce the time complexity from 
#     O(n^2) brute force to O(n) linear time."
# 2. "By using a dictionary to store indices, we trade space for speed."
# 3. "The 'complement' logic is a powerful pattern that I can apply to 
#     more complex problems like '3Sum' or '4Sum'."
# 4. "I handle the index and value mapping simultaneously to keep the 
#     algorithm clean and efficient."   