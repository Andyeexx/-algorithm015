def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count=0
        i,j=0,0

        while(i<len(g) and j<len(s)):
            if(g[i]<=s[j]):
                i+=1
                count+=1
            j+=1
        return count