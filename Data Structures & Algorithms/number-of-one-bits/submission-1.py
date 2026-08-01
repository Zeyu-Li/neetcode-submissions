class Solution:
    def hammingWeight(self, n: int) -> int:
        # time complexity since we assumed 32 bits, O(1) because fixed
        # space O(1) defined
        count = 0
        for i in range(32):
            if n % 2 == 1:
                count += 1
            n = n >> 1

        return count