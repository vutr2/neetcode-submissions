class Solution:
    def isValid(self, s: str) -> bool: 
        hash = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        stack = []

        for c in s:
            if c in "([{":
                stack.append(c)

            else:
                if not stack or stack[-1] != hash[c]:
                    return False
                stack.pop()
            
        return len(stack) == 0
            
