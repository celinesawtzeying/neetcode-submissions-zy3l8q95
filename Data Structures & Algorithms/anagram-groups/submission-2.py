"""
PROBLEM: 49. Group Anagrams
PATTERN: Arrays & Hashing (Categorization by Sorted Key)
DIFFICULTY: 🟡 Medium

-------------------------------------------------------------------------------
THE "AHA!" MOMENT:
Two strings are anagrams if they are identical after being sorted. By using the 
sorted version of a string as a "key" in a hash map (dictionary), we can 
group all original strings that share that same key.
-------------------------------------------------------------------------------

REVISION LOG:
- Key Choice: Sorting a string takes O(k log k). For very long strings, 
  using a tuple of character counts (size 26) would be more efficient O(k).
- Data Structure: Using 'defaultdict(list)' from collections avoids 
  KeyError and makes the code cleaner.
-------------------------------------------------------------------------------
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            key = "".join(sorted(s))

            if key in res:
                res[key].append(s)
            else:
                res[key] = [s]

        return list(res.values())
"""
    COMPLEXITY ANALYSIS:
    
    n = number of strings in 'strs'
    k = maximum length of a string in 'strs'

    Time Complexity: O(n * k log k)
    - We iterate through 'n' strings. 
    - For each string, we sort it, which takes O(k log k).

    Space Complexity: O(n * k)
    - We store all characters of the input in our hash map.
    """      