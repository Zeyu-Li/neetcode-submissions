class Solution:

    def encode(self, strs: List[str]) -> str:
        # niave: easy way, use a non ascii character like emoji in utf 8 to break apart

        # based on common encoding methods, encode info into str
        # first length of list, also encode legnth of each element of list

        # we can also pad with 0 given str len > 100 and len(str) > 200
        str_constructor = f"{len(strs):03}" 
        for _str in strs:
            str_constructor += f"{len(_str):03}{_str}"
        return str_constructor
    def decode(self, s: str) -> List[str]:
        ptr = 3
        count = int(s[:3])
        items = []
        while ptr < len(s):
            size = int(s[ptr:ptr+3])
            items.append(s[ptr+3:ptr+3+size])
            ptr += 3 + size
        return items
