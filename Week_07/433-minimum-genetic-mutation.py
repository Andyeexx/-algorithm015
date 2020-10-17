def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank: return -1
        alter=['A','C','G','T']
        front=[start]
        back=[end]
        step=1
        while(front):
            new_front=[]
            for node in front:
                for i in range(len(node)):
                    for alt in alter:
                        new= node[:i]+alt+node[i+1:]
                        if new in back:
                            return step
                        if(new in bank):
                            bank.remove(new)
                            new_front.append(new)
            front=new_front
            step+=1
            if len(back)<len(front):
                front,back=back,front
        return -1