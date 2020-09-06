class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans=[]
        stack=[(0,root)]
        while(stack):
            flag,node=stack.pop()
            if(node is None): continue
            if(flag==0):
                stack.append((0,node.right))
                stack.append((1,node))
                stack.append((0,node.left))
            else:
                ans.append(node.val)
        return ans