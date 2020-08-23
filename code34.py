'''
斐波那契序列
'''
class Solution:
    def __init__(self):
        self.a=[0]*100
        self.a[1]=1
    def digui(self,n):  #第一种方法：递归的暴力解法
        if n<=0:return 0
        if n==1:return 1
        return self.digui(n-1)+self.digui(n-2)

    def digui_new(self,n):
        if n<=0:return self.a[0]
        if self.a[n]!=0:return self.a[n]
        self.a[n]=self.digui_new(n-1)+self.digui_new(n-2)
        return self.a[n]




    def dynamic(self,n): #自底向上的动态规划问题
        if n<=0:return 0
        elif n<=2:return 1
        a=1
        b=1
        for i in range(3,n+1):
            tmp=b
            b=a+b
            a=tmp
        return b % 1000000007

while True:
    try:
        S=Solution()
        n=int(input())
        print(S.digui_new(n))
    except:
        break