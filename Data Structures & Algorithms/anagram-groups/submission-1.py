class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # since there is sorting, O(n * m log m)
        # O(n * m)
        groups = []
        index = {}
        for _str in strs:
            group = {}
            for char in _str:
                group[char] = group.get(char, 0) + 1
            
            hashable_dict = tuple(sorted(group.items()))
            if hashable_dict in index:
                groups[index[hashable_dict]] += [_str]
            
            else:
                index[hashable_dict] = len(groups)
                groups.append([_str])
        
        return groups