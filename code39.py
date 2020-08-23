'''
合并两个升序排列的单链表
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 if l1 else l2
        if l1.val<=l2.val:
            head=l1
            l1=l1.next
        else:
            head=l2
            l2=l2.next
        p=l1
        q=l2
        tmp=head
        while p and q:
            if p.val<=q.val:
                tmp.next=p
                tmp=tmp.next
                p=p.next
            else:
                tmp.next=q
                tmp=tmp.next
                q=q.next
        if p:
            tmp.next=p
        elif q:
            tmp.next=q
        return head

S=Solution()
l1=ListNode(1)
l1.next=ListNode(2)
l1.next.next=ListNode(3)
l2=ListNode(2)
l2.next=ListNode(4)
l2.next.next=ListNode(5)
head=S.mergeTwoLists(l1,l2)
while head:
    print(head.val)
    head=head.next

