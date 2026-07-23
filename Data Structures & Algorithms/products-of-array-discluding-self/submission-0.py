class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force is O(n^2)
        # dp, cache previously computed multiplications

        # time complexity O(n) 3 scans basically
        # memory O(n)
        # maintain cache of left and right
        l_lru = {0: nums[0]}
        r_lru = {len(nums) - 1: nums[-1]}
        # populate l and r cache and do linear run left to right
        for i in range(1, len(nums)):
            l_lru[i] = l_lru[i-1] * nums[i]

            end = len(nums) - 1 - i
            r_lru[end] = r_lru[end + 1] * nums[end]
        
        ret = []
        # do 1 final scan through
        for i, num in enumerate(nums):
            # 2 special cases at the end
            if i == 0:
                ret.append(r_lru[1])
                continue
            if i == len(nums) - 1:
                ret.append(l_lru[i - 1])
                continue
            mult = l_lru[i - 1] * r_lru[i + 1]
            ret.append(mult)

        return ret
