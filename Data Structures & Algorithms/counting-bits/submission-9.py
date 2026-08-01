class Solution:
    cache = {0: 0, 1: 1}
    x = 1
    def compute(self, n: int) -> int:
        # base case, no cache, then use hammingWeight
        if n <= 1:
            return n

        # if power of 2
        if self.x * 2 == n:
            self.x = n

        # else, using cache
        # find the closest floor power of 2 (x)
        self.cache[n] = self.cache[n - self.x] + 1
        return self.cache[n]

    def hammingWeight(self, n: int) -> int:
        # time complexity since we assumed 32 bits, O(1) because fixed
        # space O(1) defined
        count = 0
        for i in range(32):
            if n % 2 == 1:
                count += 1
            n = n >> 1

        return count
    def countBits(self, n: int) -> List[int]:
        # therefore if we do n number of times it is O(n * 1) = O(n)
        # space complexity is O(n)
        # return [self.hammingWeight(i) for i in range(n + 1)]

        # we can do better via caching.
        # notice how repeating patterns happens at every power of 2, so we can cache 
        # and only reculate one per each n^2 cycle 
        # time complexity will be O(n)
        # space complexity will be O(n) since we need to store it
        return [self.compute(i) for i in range(n+1)]
        
# class Solution:
#     cache = []
#     x = 1
#     def compute(self, n: int) -> int:
#         # base case, no cache, then use hammingWeight
#         # if n <= 1:
#         #     return n

#         # if power of 2
#         if self.x ** 2 == n:
#             self.x = n

#         # else, using cache
#         # find the closest floor power of 2 (x)
#         self.cache[n] = self.cache[n - self.x] + 1
#         return self.cache[n]

#     def hammingWeight(self, n: int) -> int:
#         # time complexity since we assumed 32 bits, O(1) because fixed
#         # space O(1) defined
#         count = 0
#         for i in range(32):
#             if n % 2 == 1:
#                 count += 1
#             n = n >> 1

#         return count
#     def countBits(self, n: int) -> List[int]:
#         # therefore if we do n number of times it is O(n * 1) = O(n)
#         # space complexity is O(n)
#         # return [self.hammingWeight(i) for i in range(n + 1)]
#         self.cache = [0] * (n+1)

#         # we can do better via caching.
#         # notice how repeating patterns happens at every power of 2, so we can cache 
#         # and only reculate one per each n^2 cycle 
#         # time complexity will be O(logn)
#         # space complexity will be O(n) since we need to store it
#         return [self.compute(i) for i in range(n+1)]
        