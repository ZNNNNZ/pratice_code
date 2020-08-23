'''
请实现一个算法可以将任一给定的数组元素反转，
如给定数组 [1, 3, 5, 2, 6] 输出为 [6, 2, 5, 3, 1]，
要求O(1) 的空间复杂度。
'''
class Soulution:
    def transverse(self,nums):
        if not nums:return nums
        length=len(nums)
        for i in range(length//2):
            nums[i],nums[length-i-1]=nums[length-i-1],nums[i]
        return nums
'''
题目描述
（编程题）给定一个正整数序列，请尝试通过将它们重新排列，
组合成一个最小的整数。例如输入为数组 [3, 6, 9, 12]，返回值为12369。
由于有可能会超出整数最大范围，所以请返回字符串类型。
'''
class min_num:
    def minnums(self,arrays):
        if not arrays:return
        for i in range(len(arrays)):
            

S=Soulution()
arrays=eval(input())
# arrays=[3,2,4,5]
print(S.transverse(arrays))
