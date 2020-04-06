# 如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，\
# 那么中位数就是所有数值排序之后位于中间的数值。\
# 如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。\
# 我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。
class Solution:
    def Insert(self, num):
        self.list=[]
        for i in range(len(num)):
            self.list.append(num[i])
            median=self.GetMedian()
            if i<len(num)-1:
                print(median,end=" ")
            else:
                print(median)

    def GetMedian(self):
        n=len(self.list)
        self.list.sort()
        if n%2==0:
            return ((self.list[n//2-1]+self.list[n//2])/2)
        else:
            return self.list[n//2]
    # def __init__(self):
    #     self.list = []
    #
    # def Insert(self, num):
    #     self.list.extend(num)
    #
    # def GetMedian(self):
    #     n = len(self.list)
    #     self.list.sort()
    #     if n % 2 == 0:
    #         return ((self.list[n // 2 - 1] + self.list[n // 2]) / 2)
    #     else:
    #         return self.list[n // 2]

S=Solution()
input1=[5,2,3,7,9,0,7,6,5,90]
S.Insert(input1)
out=S.GetMedian()
print(out)
