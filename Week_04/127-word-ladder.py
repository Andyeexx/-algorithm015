def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        length,generaldict=len(beginWord), collections.defaultdict(list)
        for word in wordList:
            for i in range(length):
                generaldict[word[:i]+'*'+word[i+1:]].append(word)
        
        markdict=collections.defaultdict(bool)
        queue=[(beginWord,1)]
        while(queue):
            word,step=queue.pop(0)
            for i in range(length):
                for neighbor in generaldict[word[:i]+'*'+word[i+1:]]:
                    if neighbor==endWord: return step+1
                    if(not markdict[neighbor]):
                        markdict[neighbor]=True
                        queue.append((neighbor,step+1))
        return 0