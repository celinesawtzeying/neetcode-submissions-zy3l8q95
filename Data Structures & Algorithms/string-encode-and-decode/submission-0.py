# use the length of the string as the start
# use '#' as the delimiter of the string

# things i got wrong
# (e.g., "10#HelloWorld"). s[i] would only grab the "1", not the "10"
class Solution:
    def encode(self, strs: List[str]) -> str:
        encode_strs = ""
        for string in strs:
            encode_strs += str(len(string)) + '#' + string 
        return encode_strs

# "5#Hello5#World"
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            res.append(word)
            i = j+1+length
        return res
                


        



