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
        # step 1: count the frequency of each number
        # use a dictionary where key = number, value = count
        freq_map = {}
        for n in nums:
            freq_map[n] = freq_map.get(n,0) + 1
        
        # step 2: convert dict into tuple 
        items = list(freq_map.items())

        # step 3: sort the list based on the freq
        # x = tuples eg.(num, freq), x[1] is freq
        # reverse = True put highest freq at the start
        items.sort(key=lambda x:x[1], reverse=True)

        return list(items[i][0] for i in range(k))

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