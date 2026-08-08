class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        maxLen = 0

        for num in nums:
            if(num-1 not in numbers):
                tempNum = num
                tempLen = 0
                while tempNum in numbers:
                    tempLen += 1
                    tempNum += 1

                if tempLen > maxLen:
                    maxLen = tempLen

        return maxLen