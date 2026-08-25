class Solution:
    def isBalanced(self, s):
        # code here
        matching={')':'(','}':'{',']':'['}
        stack=[]
        for char in s:
            if char not in matching:
                stack.append(char)
            else:
                if not stack:
                    return False
                if stack.pop()!=matching[char]:
                    return False
        return len(stack)==0
            