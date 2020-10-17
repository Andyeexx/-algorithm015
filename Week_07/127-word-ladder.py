def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        length,generaldict=len(beginWord), collections.defaultdict(list)
        for word in wordList:
            for i in range(length):
                generaldict[word[:i]+'*'+word[i+1:]].append(word)
        markdict=set()
        markdict.add(endWord)
        front=[beginWord]
        back=[endWord]
        step=2
        while front:
            new_front=[]
            for word in front:
                for i in range(len(word)):
                    for next_word in generaldict[word[:i]+'*'+word[i+1:]]:
                        if(next_word) in back:
                            return step
                        if next_word not in markdict:
                            new_front.append(next_word)
                            markdict.add(next_word)
            front=new_front
            step+=1
            if(len(back)<len(front)):
                front,back=back,front
        return 0