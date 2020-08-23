'''
输入两个整数序列，第一个序列表示栈的压入顺序，
请判断第二个序列是否可能为该栈的弹出顺序。
假设压入栈的所有数字均不相等。
例如序列1,2,3,4,5是某栈的压入顺序，
序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。
（注意：这两个序列的长度是相等的）
'''
class Ismatch():
    def match_p(self,arrs1,arrs2):
        if len(arrs1)!=len(arrs2):return False
        if (not arrs1) or (not arrs2):return False
        list1=[]
        for i in arrs1:
            if i==arrs2[0]:
                del(arrs2[0])
            else:
                list1.append(i)
        if not list1 and not arrs2:return True
        else:
            list1.reverse()
            if list1==arrs2:return True
            else:return False
I=Ismatch()
print(I.match_p([1,2,3,4,5],[1,2,3,4,5]))