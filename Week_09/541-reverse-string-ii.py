def reverseStr(self, s: str, k: int) -> str:
        if not s or not k: return s
        count=0
        s=list(s)

        def swap(start,end):
            while(start<end):
                s[start],s[end]=s[end],s[start]
                start+=1
                end-=1

        while count<len(s):
            remain=len(s)-count
            if remain>=2*k:
                swap(count,count+k-1)
            elif k<=remain<2*k:
                swap(count,count+k-1)
                break
            else:
                swap(count,len(s)-1)
                break
            count+=2*k
        
        return ''.join(s)