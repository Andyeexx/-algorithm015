def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not words: return []
        trie={}
        ans=set()
        for word in words:
            node=trie
            for c in word:
                node=node.setdefault(c, {})
            node["#"]=True

        def dfs(i,j,pre,node,visited):
            if "#" in node:
                ans.add(pre)
            for dirx,dirj in [(1,0),(0,1),(-1,0),(0,-1)]:
                _i,_j=i+dirx,j+dirj
                if 0<=_i<max_row and 0<=_j<max_col and board[_i][_j] in node and (_i,_j) not in visited:
                    visited.add((_i,_j))
                    dfs(_i,_j,pre+board[_i][_j],node[board[_i][_j]],visited)
                    visited.remove((_i,_j))
            
        max_row,max_col=len(board),len(board[0])
        for i in range(max_row):
            for j in range(max_col):
                if board[i][j] in trie:
                    dfs(i,j,board[i][j],trie[board[i][j]],{(i,j)})
        return list(ans)