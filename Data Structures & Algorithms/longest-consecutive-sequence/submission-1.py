class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sort and linear scan for longest max(previous_record, candidate)
        nums = list(sorted(set(nums)))
        

        if len(nums) <= 1:
            return len(nums)

        _max = 1
        candidate = 1
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == prev + 1:
                candidate += 1
            else:
                candidate = 1
            
            _max = max(_max, candidate)
            prev = nums[i]
        
        return _max