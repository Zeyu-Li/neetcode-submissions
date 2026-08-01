class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # time complexity O(n)
        # space complexity O(n) because we have to construct the set
        # base case
        if len(nums) <= 1:
            return len(nums)

        # convert to a set and check left most neighbour
        numSet = set(nums)
        _max = 1
        for num in nums:
            if num - 1 in numSet:
                # skip it, it is not the start of a sequence
                continue
            # check length
            counter = 1
            curr = num
            while curr + 1 in numSet:
                counter += 1
                curr += 1
            _max = max(_max, counter)
        
        return _max

# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         # sort is O(nlogn)
#         # space complexity is O(n)
#         # sort and linear scan for longest max(previous_record, candidate)
#         nums.sort()
        

#         if len(nums) <= 1:
#             return len(nums)

#         _max = 1
#         candidate = 1
#         prev = nums[0]
#         for i in range(1, len(nums)):
#             if nums[i] == prev + 1:
#                 candidate += 1
#             elif nums[i] == prev:
#                 continue
#             else:
#                 candidate = 1
            
#             _max = max(_max, candidate)
#             prev = nums[i]
        
#         return _max