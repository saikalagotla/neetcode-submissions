class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        savedNums = {}
        ret = []
        for i in range(len(nums)):
            lookFor = target-nums[i]
            if (savedNums.get(lookFor) != None):
                ret = [savedNums[lookFor], i]
                break
            else:
                savedNums[nums[i]] = i

        return ret