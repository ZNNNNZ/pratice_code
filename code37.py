class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(left,right):
            if left >= right:
                return
            p=(left+right)//2
            root=TreeNode(nums[p])
            root.left=helper(left,p)
            root.right=helper(p+1,right)
            return root
        return helper(0,len(nums))

S=Solution()
nums=[-10,-3,0,5,9]
root=S.sortedArrayToBST(nums)
print(root.val)
print(root.left.val)
print(root.right.left.val)