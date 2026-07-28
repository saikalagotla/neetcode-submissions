class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lettersS = {}
        lettersT = {}

        if(len(s) != len(t)):
            return False

        for val in s:
            lettersS[val] = lettersS.get(val, 0) + 1
        
        for val in t:
            lettersT[val] = lettersT.get(val, 0) + 1

        for key in lettersS:
            if(lettersT.get(key) and lettersS[key] == lettersT[key]):
                continue
            else:
                return False

        return True