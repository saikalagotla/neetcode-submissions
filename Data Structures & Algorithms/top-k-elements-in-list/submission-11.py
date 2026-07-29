class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        countsDict = {}
        counts = [set() for _ in range(len(nums)+1)]

        for num in nums:
            if(countsDict.get(num) != None):
                indx = countsDict[num]
                counts[indx].remove(num)
                counts[indx+1].add(num)
                countsDict[num] = countsDict[num]+1
            else:
                countsDict[num] = 1
                counts[1].add(num)

        ret = []
        tempK = k
        for s in reversed(counts):
            for val in s:
                ret.append(val)
                tempK -= 1
                if(tempK == 0):
                    break
            
            if(tempK == 0):
                break

        return ret
            
