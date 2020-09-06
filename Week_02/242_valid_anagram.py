class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m1=collections.Counter(s)
        m2=collections.Counter(t)
        if(len(m1.keys())!=len(m2.keys()) ): return False
        for key in m1.keys():
            if(not m2.get(key) or m2[key]!=m1[key] ):
                return False
        return True