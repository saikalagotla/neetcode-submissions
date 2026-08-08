class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left = 0
        right = len(s)-1

        while(left < right):
            continueFlag = False
            if(not s[left].isalnum()):
                left += 1
                continueFlag = True
            if(not s[right].isalnum()):
                right -= 1
                continueFlag = True
            if(continueFlag):
                continue
            if(not s[left].lower() == s[right].lower()):
                return False
            left += 1
            right -= 1
        
        return True