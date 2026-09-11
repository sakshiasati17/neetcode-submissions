class Solution:
    def isValid(self, s: str) -> bool:
        freq={'(': ')', '{': '}', '[' : ']'}
        stack=[]
        for i in range(len(s)):
            if s[i] in freq:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                if freq[stack[-1]]!=s[i]:
                    return False
                stack.pop()
        return not stack
                    
                    
