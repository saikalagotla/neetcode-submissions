class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequencies = {}

        for number in nums:
            frequencies[number] = 1 + frequencies.get(number, 0)

        a = [[] for _ in range(len(nums))]

        for key in frequencies.keys():
            index = frequencies[key]-1
            a[index].append(key)
        
        print(a[::-1])

        ret = []
        for nums in a[::-1]:
            if(k == 0):
                break
            if(len(nums) > 0):
                for num in nums:
                    if(k == 0):
                        break
                    ret.append(num)
                    k = k-1
        
        return ret
