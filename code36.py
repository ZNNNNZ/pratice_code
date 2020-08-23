'''
判断是否为二叉搜索树
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(root,lower=float('-inf'),upper=float('inf')):
            if not root:
                return True
            if root.val<=lower or root.val>=upper:
                return False
            if not helper(root.left,lower=lower,upper=root.val):#左子树的上界要改为根节点的值，同时不能超过下界
                return False
            if not helper(root.right,lower=root.val,upper=upper):#右子树同理，下界要改为根节点的值
                return False
            return True
        return helper(root)


class Solution1:#（不是很清晰的理解代码的意思）
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack, inorder = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # 如果中序遍历得到的节点的值小于等于前一个 inorder，说明不是二叉搜索树
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True


root=TreeNode(2)
root.left=TreeNode(1)
root.right=TreeNode(4)
root.left.right=TreeNode(3)
S=Solution1()
print(S.isValidBST(root))

