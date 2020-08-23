'''
# 数轴覆盖
**题目：**给定一个数轴arr,数轴中有n个数arr[0],arr[1],arr[2]....arr[n-1]，
给定一个长度为L的绳子，要求绳子能在数轴上覆盖到的最多的点的个数；
**思路：**
- 双指针Left和Right，从数轴上的第一个点开始；
- Left固定，Right向后移动，直到(Right-Left)的长度超过绳子的长度L之后，就将左指针Left向后移动一格；
- 重复以上操作，直到左指针Left指到尾端
'''
class Solution:
    def shuzhoufugai(self,arrs,L):
        if not arrs or L<=0:return
        left=0
        right=0
        max_nodes=0
        N=len(arrs)
        while left<N:
            while right<N and (arrs[right]-arrs[left])<=L:
                right+=1
            max_nodes=max(max_nodes,right-(left))#这里right其实多加了1，但是点个数为右坐标-左坐标+1；
            left += 1
        return max_nodes

S=Solution()
arrs=list(eval(input('请输入数轴：')))
L=int(input('请输入绳子长度：'))
print(S.shuzhoufugai(arrs,L))