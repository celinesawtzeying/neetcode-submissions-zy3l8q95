"""
Step A: Find the Delimiter (#)
Use a second pointer j starting at i. Move j forward until s[j] == "#". This identifies the end of the "length" portion.

Step B: Extract the Length
Slice the string from i to j (the characters before the #) and convert it to an integer.

length = int(s[i:j])

Step C: Extract the Word
Use the length to slice the exact portion of the string that contains the word. Remember: the word starts at j + 1.

word = s[j + 1 : j + 1 + length]

Step D: Leapfrog to the Next Segment
Update your main pointer i to point to the start of the next length prefix.

i = j + 1 + length

#################################
    COMMON PITFALLS
#################################
1. (e.g., "10#HelloWorld"). s[i] would only grab the "1", not the "10"
2. slice inclusive first then exclusive
|  H  |  e  |  l  |  l  |  o  |
 0     1     2     3     4     5
If you want "Hel", you go from boundary 0 to boundary 3.
s[0:3] gives you indices 0, 1, and 2. It excludes index 3

"""
class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

# "5#Hello5#World"
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j + 1:j+ length + 1]
            res.append(word)
            i = j + length + 1

        return res
                


        



