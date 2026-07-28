class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for i in range(len(s)):
            print(stack)
            if(len(stack) == 0):
                stack.append(s[i])
            elif (ord(s[i]) == ord(stack[0])+1 or ord(s[i]) == ord(stack[0])+2):
                stack.pop(0)
            else:
                stack.insert(0,s[i])
        
        print(stack)
        return len(stack) == 0