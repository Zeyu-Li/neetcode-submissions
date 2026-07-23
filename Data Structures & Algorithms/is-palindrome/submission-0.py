class Solution:
    def isPalindrome(self, s: str) -> bool:
        # you can do 2 pointer but easiest to create another reverse object and check
        # this adds O(n) memory but time complexity does not change

        # filter out all non alphanumeric characters
        s_filtered = []
        for char in s:
            if char.isalnum():
                s_filtered.append(char.lower())

        res_s = s_filtered[::-1]

        for char1, char2 in zip(res_s, s_filtered):
            if char1 != char2:
                return False

        return True