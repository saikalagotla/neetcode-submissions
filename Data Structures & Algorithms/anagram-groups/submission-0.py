class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        allGroups = {}

        for word in strs:
            sortedWord = "".join(sorted(word))
            if(allGroups.get(sortedWord) != None):
                allGroups[sortedWord].append(word)
            else:
                allGroups[sortedWord] = [word]

        return list(allGroups.values())