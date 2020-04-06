#题目要求：输入一个链表，输出该链表中倒数第k个结点
#在这里我自己创建出一个链表
class Node(object):
    """单链表的结点"""
    def __init__(self, item):
        # item存放数据元素
        self.item = item
        # next是下一个节点的标识
        self.next = None
class SingleLinkList(object):
    """单链表"""
    def __init__(self):
        self._head = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        i=0
        node=head
        while node!=None:
            node=node.next
            i=i+1
        if k>i or k<1:
            return
        j=1
        while j<i-k+1:
            head=head.next
            j=j+1
        return head

linklist=SingleLinkList()
node1=Node(1)
linklist._head=node1
node2=Node(2)
node1.next=node2
node3=Node(3)
node2.next=node3
node4=Node(4)
node3.next=node4
# print(node3.next.item)
S=Solution()
nodek=S.FindKthToTail(node1,4)
print(nodek.item)