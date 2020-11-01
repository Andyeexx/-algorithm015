
def firstUniqChar(self, s: str) -> int:
        if not s: return -1
        dic= collections.Counter(s)
        if 1 in list(dic.values()):
            index=list(dic.values()).index(1)
        else:
            return -1
        char=list(dic.keys())[index]
        return s.find(char)