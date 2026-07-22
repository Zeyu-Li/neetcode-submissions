class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s_contains = {}
        t_contains = {}
        for s1 in s:
            s_contains[s1] = s_contains.get(s1, 0) + 1
        
        for t1 in t:
            t_contains[t1] = t_contains.get(t1, 0) + 1

        for k, v in s_contains.items():
            if t_contains.get(k, 0) != v: return False

        return True