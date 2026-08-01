import math
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 0, 1, 10, 11, 100, 101, 110, 111, 1000 - X
        # notice a pattern, you will 0 out if you xor up to 2**n
        # we can use this pattern to determine the missing one because the
        # xor illumenates the missing one

        # question, are they given in order
        _max = len(nums)
        c = 0

        for num in nums:
            c ^= num
        
        for i in range(len(nums) + 1):
            c ^= i
        return c
        
        # we then need to xor the last block from the last n^2
        # then xor the remaining numbers to get 0 since Y ^ Y = 0
        last = nums[-1]
        c = 0
        while last != 0: 
            last >>= 1
            c+=1
        for i in range(c, _max + 1):
            c ^= i


        return c