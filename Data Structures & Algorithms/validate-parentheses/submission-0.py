class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")":"(", "}":"{", "]" : "["}

        for char in s:
            # check if it's one of the key
            if char in mapping:
                if stack:
                    top = stack.pop()
                else:
                    top = "#"
                
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)
        if stack:
            return False
        else:
            return True