class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set()

        for num in nums:
            numbers.add(num)

        startOfSequences = []

        for num in nums:
            if(num-1 not in numbers):
                startOfSequences.append(num)

        maxLen = 0
        for num in startOfSequences:
            tempNum = num
            tempLen = 0
            while tempNum in numbers:
                tempLen += 1
                tempNum += 1

            if tempLen > maxLen:
                maxLen = tempLen

        return maxLen