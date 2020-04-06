'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0
        n=len(rotateArray)
        min1=rotateArray[0]
        minj=0
        i=1
        while i<n:
            if min1<rotateArray[i]:
                i=i+1
            else:
                min1=rotateArray[i]
                minj=i
                i=i+1
        new_array=rotateArray[minj:]+rotateArray[:minj]
        return new_array

S=Solution()
rotatearray= list(eval(input('请输入非递减数组：')))
# rotatearray=[3,5,4,2,3]
new_array=S.minNumberInRotateArray(rotatearray)
print(new_array)
print('the min of this array: %f'%(new_array[0]))
