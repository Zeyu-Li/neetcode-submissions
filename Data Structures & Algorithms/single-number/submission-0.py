class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # bitwise xor operations. Note xor a number with itself will return 0
        xor_sum = 0
        for num in nums:
            xor_sum ^= num

        return xor_sum