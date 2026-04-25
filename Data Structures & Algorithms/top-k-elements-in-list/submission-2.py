"""
PROBLEM: 347. Top K Frequent Elements
PATTERN: Arrays & Hashing (Frequency Map + Sorting)
DIFFICULTY: 🟡 Medium

-------------------------------------------------------------------------------
THE "AHA!" MOMENT:
To find the 'Top K' elements, we must first know how many times each element 
appears. A Hash Map (Dictionary) is the most efficient way to store these 
counts. Once we have the frequencies, we sort them to find the highest values.
-------------------------------------------------------------------------------

REVISION LOG:
- BUG FIX: Moved sorting and return logic OUTSIDE the for loop.
- Manual Initialization: Used a standard dict with .get() to avoid 'collections'.
- Sorting Logic: Used .sort() in-place on the items list for better memory efficiency.
-------------------------------------------------------------------------------
"""

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count_map = {}

        # Step 1: Build the full frequency map
        for n in nums:
            count_map[n] = count_map.get(n, 0) + 1

        # Step 2: Convert to a list of tuples AFTER the loop finishes
        items = list(count_map.items())

        # Step 3: Sort by frequency (x[1]) in descending order
        items.sort(key=lambda x: x[1], reverse=True)

        # Step 4: Extract the top 'k' elements
        return [items[i][0] for i in range(k)]

    """
    COMPLEXITY ANALYSIS:
    
    Time Complexity: O(n + u log u)
    - O(n) to iterate through the input list and build the map.
    - O(u log u) to sort the unique elements (u), where u <= n.

    Space Complexity: O(u)
    - We store the counts of unique elements in a dictionary.
    """

# --- INTERVIEW TALKING POINTS ---
# 1. "I ensured the frequency map was fully constructed before sorting to 
#     guarantee accurate counts."
# 2. "I used .sort() on the items list rather than sorted() to perform the 
#     operation in-place, which is more memory-efficient."
# 3. "While this O(u log u) approach is very clean, I could further optimize 
#     this to O(n) using Bucket Sort or O(n log k) using a Min-Heap."