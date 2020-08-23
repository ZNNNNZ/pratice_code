'''
删除排序数组中的重复项;
给定一个排序数组，你需要在 原地 删除重复出现的元素，
使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 ,
并在使用 O(1) 额外空间的条件下完成。
'''
class Solution(object):
    '''def removeDuplicates(self, nums):
        if not nums:return
        i=0
        while i < (len(nums)-1):
            j=i+1
            if nums[i]==nums[j]:
                del(nums[j])
            else:
                i=i+1
        return len(nums)'''

    def removeDuplicates(self, nums): #根据题解优化算法/双指针方法
        if not nums:return
        i=0
        j=1
        while j < len(nums):
            if nums[i]!=nums[j]:
                if j-i>1:
                    nums[i+1]=nums[j]
                i=i+1
            j=j+1
        return (i+1)

S=Solution()
nums=[1]
l=S.removeDuplicates(nums)
print(l)
for i in range(l):
    print(nums[i])
