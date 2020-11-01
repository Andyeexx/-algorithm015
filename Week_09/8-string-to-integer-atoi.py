def myAtoi(self, string: str) -> int:
        string= string.strip()
        negative=False
        if not string: return 0
        if(string[0]=='-' or string[0]=='+'):
            pass
        elif(not string[0].isdigit()):
            return 0
        pos=1
        while pos<len(string):
            if(string[pos].isdigit()):
                pos+=1
            else:
                break
        if(pos==1 and not string[0].isdigit()): return 0
        ans=int(string[:pos])
        if(ans>2**31-1):return 2**31-1
        if(ans<-2**31):return -2**31
        return ans