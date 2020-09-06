class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if(not root):return None
        ans=[]
        def helper(node,level):
            if len(ans)==level:
                ans.append([])
            ans[level].append(node.val)
            for child in node.children:
                helper(child,level+1)
        helper(root,0)
        return ans
        