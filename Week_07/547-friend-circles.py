def findCircleNum(self, M: List[List[int]]) -> int:
        if not M: return 0
        parent=[i for i in range(len(M))]
        def find(i):
            root=i
            while (parent[root]!=root):
                root=parent[root]
            while (parent[i]!=i):
                parent[i],i=root, parent[i]
            return root
            
        def union(i,j):
            a=find(i)
            b=find(j)
            parent[b]=a

        for i in range(len(M)):
            for j in range(len(M)):
                if(i!=j and M[i][j]==1):
                    union(i,j)
        
        return len(set([find(i) for i in range(len(M))]))
