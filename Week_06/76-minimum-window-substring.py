def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t)>len(s):return ""
        ans=(0,float('inf'))
        i=0
        need=collections.defaultdict(int)
        needct=0
        for c in t:
            need[c]+=1
            needct+=1
        for j,c in enumerate(s):
            if needct>0:
                if(need[c]>0):
                    needct-=1
                need[c]-=1
            if needct==0:
                while True:
                    char=s[i]
                    if(need[char]==0):
                        break
                    need[char]+=1
                    i+=1
                if(ans[1]-ans[0]>j-i):
                    ans=(i,j)
                needct+=1
                need[s[i]]+=1
                i+=1

        return s[ans[0]:ans[1]+1] if ans[1]!=float('inf') else ""