class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""
        for s in strs:
            res += str(len(s))+"#"+s
        return res

    def decode(self, s: str) -> List[str]:

        print(s)
        res = []
        i = 0
        while i < len(s):
            strLen = ""
            while s[i] != "#":
                strLen += s[i]
                i += 1
            strLen = int(strLen)
            print(s[i+1:i+1+strLen])
            res.append(s[i+1:i+1+strLen])
            i += strLen+1
        
        return res