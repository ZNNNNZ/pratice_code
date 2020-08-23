class merge_array:
    def mergearray(self,nums,arr1,arr2):
        num1=nums[0]
        num2=nums[1]
        new_list=[]
        i=0
        j=0
        while i<num1 and j<num2:
            if arr1[i]<=arr2[j]:
                new_list.append(arr1[i])
                i=i+1
            else:
                new_list.append(arr2[j])
                j=j+1
        if i<num1:
            new_list.extend(arr1[i:])
        if j <num2:
                new_list.extend(arr2[j:])
        return new_list
'''
假设有一个有 n 个元素的数组，求该数组右移 k 个元素后的数组，要求算法的空间复杂度为 O(1) 。

输入数据右三行，第一行表示数组元素个数 n ，第二行表示数组，第三行表示 k

7

1,2,3,4,5,6,7

3

输出

5,6,7,1,2,3,4
'''
class roate:
    def roatearrays(self,n,arrays,k):
        if k==0:
            return arrays
        if k%n==0:
            return arrays
        i=k%n
        for j in range(n-i,n):
            left=j-(n-i)
            for k in range(left,j)[::-1]:
                arrays[k],arrays[k+1]=arrays[k+1],arrays[k]
        return arrays

S=merge_array()
R=roate()
# nums=list(eval(input('请输入两个序列的长度')))
# arrays1=list(eval(input('请输入序列1')))
# arrays2=list(eval(input('请输入序列2')))
# print(S.mergearray(nums,arrays1,arrays2))
n=int(input())
arrays=list(eval(input()))
k=int(input())
print(R.roatearrays(n,arrays,k))