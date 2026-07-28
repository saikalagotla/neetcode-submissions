class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numLen = len(nums)

        left = [0 for _ in range(numLen)]
        right = [0 for _ in range(numLen)]

        left[0] = nums[0]
        right[numLen-1] = nums[numLen-1]
        i = 1
        while i < numLen:
            left[i] = left[i-1]*nums[i]
            right[numLen-i-1] = right[numLen-i]*nums[numLen-i-1]
            i += 1

        print(left, right)

        res = []
        x = 0
        while x < numLen:
            if(x == 0):
                res.append(right[1])
            elif(x == numLen-1):
                res.append(left[numLen-2])
            else:
                res.append(left[x-1]*right[x+1])
            
            x += 1
        
        return res