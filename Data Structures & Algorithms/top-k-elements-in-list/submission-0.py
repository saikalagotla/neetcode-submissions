class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mostFrequent = {}

        for number in nums:
            mostFrequent[number] = 1 + mostFrequent.get(number, 0)

        sorted_vals = sorted(mostFrequent.keys(), key=lambda number: mostFrequent[number])

        print(sorted_vals)

        return sorted_vals[len(sorted_vals)-(k):]
        
