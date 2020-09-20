def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if(not wordList or endWord not in wordList):return []

        length,generaldict=len(beginWord),collections.defaultdict(list)
        for word in wordList:
            for i in range(length):
                generaldict[word[:i]+'*'+word[i+1:]].append(word)
        markdict=collections.defaultdict(bool)

        queue=[(beginWord,1,[beginWord])]
        lowest_step=-1
        ans=[]
        while(queue):
            word, step,curlist= queue.pop(0)
            if(lowest_step!=-1 and  step>lowest_step): break
            markdict[word]=True
            for i in range(length):
                for neighbor in generaldict[word[:i]+'*'+word[i+1:]]:
                    if(neighbor==endWord):
                        if(lowest_step==-1):
                            lowest_step=step
                            ans.append(curlist+[neighbor])
                        elif(lowest_step!=-1 and step==lowest_step):
                            ans.append(curlist+[neighbor])
                    elif(not markdict[neighbor]):
                        queue.append((neighbor,step+1,curlist+[neighbor]))
        if(ans):return ans
        return []