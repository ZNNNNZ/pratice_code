'''
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点
（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
'''

#深度遍历方法（DFS），递归思路
class Solution:
    def TreeDepth(self, pRoot):
        if pRoot is None:
            return 0
        return max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1

    #广度遍历方法（BFS）
    def max_depth(self,root):
        if root is None:return 0
        gen=[root]
        res=0
        while gen:
            tmp=[]
            for node in gen:
                if node.left:tmp.append(node.left)
                if node.right:tmp.append(node.right)
            gen=tmp
            res+=1
        return res




