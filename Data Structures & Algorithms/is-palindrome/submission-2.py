class Solution:
    def isPalindrome(self, s: str) -> bool:
        ptr1 = 0
        ptr2 = len(s) - 1
        # compare for both ends
        while ptr1 < ptr2:
            while ptr1 < len(s) and not s[ptr1].isalnum():
                ptr1 += 1
            
            while ptr2 > 0 and not s[ptr2].isalnum():
                ptr2 -= 1
            
            # check validity again
            if ptr1 >= ptr2:
                return True
            if s[ptr1].lower() != s[ptr2].lower():
                return False
            
            ptr1 += 1
            ptr2 -= 1
            
        return True
            