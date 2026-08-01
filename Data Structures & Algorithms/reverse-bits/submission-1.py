class Solution:
    def reverseBits(self, n: int) -> int:
        # one pass shifting the least sig bit
        counter = 31
        _sum = 0
        while counter >= 0:
            if n % 2:
                _sum += 2 ** counter
            n >>= 1
            counter -= 1
        
        return _sum