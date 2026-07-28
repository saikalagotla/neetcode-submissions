class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}

        for val in s:
            letters[val] = letters.get(val, 0) + 1
        
        print(letters)
        for val in t:
            if(letters.get(val) and letters[val] != 0):
                letters[val] -= 1
            else:
                return False
        for x in letters:
            if(letters[x] != 0):
                return False
            
        return True