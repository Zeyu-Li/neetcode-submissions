class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        # get frequency list
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        
        # sort order
        ordered_dict = tuple(sorted(seen.items(), key=lambda x: x[1], reverse=True))
        more_freq = [item[0] for item in ordered_dict[:k]]
        return more_freq