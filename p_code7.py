# 输入一个递增排序的数组和一个数字S，在数组中查找两个数，
# 使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        n=len(array)
        if n == 0:
            return []
        if n != 0 and tsum <= array[0]:
            return []
        mid=tsum/2
        i=0
        while array[i]<mid:
            i=i+1
        # j=i
        # for k in range(i):
        #     for m in range(j,n):
        #         if array[k]+array[m]==tsum:
        #             return [array[k],array[m]]
        k = 0
        m = n - 1
        while k < i:
            while m >= i:
                if array[k] + array[m] == tsum:
                    return [array[k], array[m]]
                elif array[k]+array[m] > tsum:
                    m = m - 1
                else:
                    k=k+1
        return None

S=Solution()
input_total=eval(input('请分别输入递增数组和数字S：'))
array1=input_total[0]
s1=input_total[1]
print(S.FindNumbersWithSum(array1,s1))