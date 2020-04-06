# #题目要求：输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
# #定义链表结点
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# class Solution:
#     # 返回从尾部到头部的列表值序列，例如[1,2,3]
#     def printListFromTailToHead(self, L):#从链表的第一个节点进入，依次访问每个节点的数值并且输入到列表中，最后输出转置的列表
#         l = list()
#         while L:
#             l.append(L.val)
#             L = L.next
#         # return l.reverse()
#         return l[::-1]
#
# L=ListNode(2)
# # input1=L.__init__(2)
# S=Solution()
# print(S.printListFromTailToHead(L))

i=[1,2,3]
# print(i[::-1])  #a[i:j:s]从i到j的数据，s表示步进，默认为1，当s为-1时，选取的数据排列为倒序
i.reverse()
print(i)