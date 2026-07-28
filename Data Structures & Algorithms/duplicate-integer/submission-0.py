class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = set()

        for val in nums:
            if(val in dups):
                return True
            else:
                dups.add(val)

        return False