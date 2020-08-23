'''
买卖股票的最佳时机II
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。
你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
示例一：
输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，
在第 3 天（股票价格 = 5）的时候卖出,
这笔交易所能获得利润 = 5-1 = 4 。
随后，在第 4 天（股票价格 = 3）的时候买入，
在第 5 天（股票价格 = 6）的时候卖出,
这笔交易所能获得利润 = 6-3 = 3 。
'''
class Solution(object):
    def maxProfit(self, prices):
        if not prices:return 0
        res=0
        for i in range(len(prices)-1):
            if prices[i+1]-prices[i]>0:
                res+=prices[i+1]-prices[i]
        return res
S=Solution()
prices=[1,6,5,4,3,2,1]
print(S.maxProfit(prices))

'''
买卖股票的最佳时机
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），
设计一个算法来计算你所能获取的最大利润。
注意：你不能在买入股票前卖出股票。
示例一：
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，
在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；
同时，你不能在买入前卖出股票。
'''
class Solution(object):
    def maxProfit(self, prices):
        if not prices:return 0
        min_=prices[0]
        max_=0
        for i in prices:     #一次遍历的方法，以每次的最小值为基准
            min_=min(min_,i)  #找到后面的数和最小值之间的差值
            max_=max(max_,i-min_) #再找出所有差值之间的最大值
        return max_
S=Solution()
p=[7,5,4]
print(S.maxProfit(p))

