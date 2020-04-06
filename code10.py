# 大家都知道斐波那契数列，现在要求输入一个整数n，
# 请你输出斐波那契数列的第n项（从0开始，第0项为0）。n<=39
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n==0:
            return 0
        if n<=2:
            return 1
        a2=1
        a3=2
        j=3
        while j<n:
            tmp=a2+a3
            a2=a3
            a3=tmp
            j=j+1
        return a3

    def Fibonacci1(self, n):
        listf=[0,1]
        for i in range(2,n+1):
            listf.append(listf[-2]+listf[-1])
        return listf[n]


S=Solution()
n=int(input())
print(S.Fibonacci1(n))