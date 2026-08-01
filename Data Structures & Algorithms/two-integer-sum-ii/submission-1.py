class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 2 pointers
        # space complexity O(1) in place
        # time complexity must be O(n) because it could be last 2 elements worst case

        # store the diff we need in place and if we find the number after, we can take it
        for i in range(len(numbers)):
            item = target - numbers[i]
            # scan if it exists after
            for j in range(i + 1, len(numbers)):
                if item == numbers[j]:
                    return [i + 1, j + 1]
            numbers[i] = item