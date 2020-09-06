class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans=[]
        stack=[root]
        while(stack):
            node=stack.pop()
            if(not node):
                return None
            for child in node.children[::-1]:
                stack.append(child)
            ans.append(node.val)
        return ans