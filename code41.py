'''
统计所有小于非负整数 n 的质数的数量。
示例:
输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
'''
'''
class Solution(object):
    def countPrimes1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return 0
        dp=[True for i in range(2,n)]
        i=2
        while i*i<n:
            if dp[i-2]:
                for j in range(i*i,n)[::i]:
                    dp[j-2]=False
            i+=1
        return sum(dp)

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        dp=[True for i in range(n)]
        dp[0]=False
        dp[1]=False
        i=2
        while i*i<n:
            if dp[i]:
                dp[i*i:n:i]=[False]*(len(dp[i*i:n:i]))
            i+=1
        return sum(dp)
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        p=head
        q=head.next
        head.next=None
        while q:
            tmp=q.next
            q.next=p
            p=q
            q=tmp
        return p
S=Solution()
node=ListNode(1)
node.next=ListNode(2)
node.next.next=ListNode(3)
# print(S.countPrimes(2))
# print(S.reverseList(node).val)
new_head=S.reverseList(node)
while new_head:
    print(new_head.val)
    new_head=new_head.next