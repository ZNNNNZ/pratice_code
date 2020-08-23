# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        elif not head.next.next:
            return (head.val==head.next.val)
        fast=head.next
        slow=head
        while fast:
            if not fast.next:
                break
            slow = slow.next
            fast=fast.next.next
        p=slow
        q=p.next
        while q:
            tmp=q.next
            q.next=p
            p=q
            q=tmp
        while p!=slow:
            if head.val!=p.val:
                return False
            head=head.next
            p=p.next
        return True

S=Solution()
l1=ListNode(1)
l1.next=ListNode(1)
l1.next.next=ListNode(2)
l1.next.next.next=ListNode(1)
print(S.isPalindrome(l1))