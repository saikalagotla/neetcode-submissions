class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        stAlphaNum = ""

        for char in s:
            if(char.isalnum()):
                stAlphaNum += char.lower()

        return stAlphaNum == stAlphaNum[::-1]