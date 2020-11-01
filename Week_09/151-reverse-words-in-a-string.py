def reverseWords(self, s: str) -> str:
        s=s.strip().split()
        front, end = 0, len(s)-1
        while(front<end):
            s[front],s[end]=s[end].strip(), s[front].strip()
            front+=1
            end-=1
        return " ".join(s)