class Solution:
    def reverseBits(self, n: int) -> int:
        # one pass shifting the least sig bit (running sum)
        # time complexity O(n) based on digits
        # space complexity O(1)
        counter = 31
        _sum = 0
        while counter >= 0:
            if n % 2:
                _sum += 2 ** counter
            n >>= 1
            counter -= 1
        
        return _sum