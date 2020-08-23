class sort_methods:
    def maopao(self,arrays):
        #冒泡排序算法
        #升序
        for i in range(len(arrays)):
            sign = False
            for j in range(len(arrays)-i-1):
                if arrays[j]>arrays[j+1]:
                    arrays[j],arrays[j+1]=arrays[j+1],arrays[j]
                    sign=True
            if not sign:
                break
        return arrays
    def fast_sort(self,arrays,left,right):
        #快速排序算法
        #升序
        if left>=right or len(arrays)==1:
            return arrays
        leftbound = left
        rightbound = right
        pivot = arrays[left]
        while(left<right):
            while (left<right and arrays[right]>=pivot):
                right=right-1
            if (left<right and arrays[right]<pivot):
                arrays[left]=arrays[right]
            while(left<right and arrays[left]<=pivot):
                left=left+1
            if (left<right and arrays[left]>pivot):
                arrays[right]=arrays[left]
            if left>=right:
                    arrays[left]=pivot
        self.fast_sort(arrays,leftbound,right-1)
        self.fast_sort(arrays,right+1,rightbound)
        return arrays
class heap_methods:
    #堆排序
    #升序
    def max_heap(self,nums,root,length):
        #输入的节点分别求左子节点和右子节点，如果i=0，表示顶端节点，left=1,right=2
        left=root*2+1
        right=root*2+2
        max_r=root
        #如果左子节点的值比max节点大，max指针换为左节点
        if left<length and nums[left]>nums[max_r]:
            max_r=left
        # 如果右子节点的值比max节点大，max指针换为右节点
        if right<length and nums[right]>nums[max_r]:
            max_r=right
        if max_r!=root:
            nums[max_r],nums[root]=nums[root],nums[max_r]
            self.max_heap(nums,max_r,length) #根节点变换后要重新往下遍历，保证大顶堆特征，即根节点一定要大于子节点

    def heap_sort(self,arrays):
        length=len(arrays)
        for k in range (length)[::-1]:#每取出一个最顶端的值后，序列长度减一
            for i in range((k+1)//2)[::-1]: #从最底层的根节点开始往上遍历，保证大顶堆特征
                self.max_heap(arrays,i,k+1)
            arrays[0],arrays[k]=arrays[k],arrays[0]#取出顶端最大值到序列尾端
        return arrays
class select_sort:
    def simple_select_sort(self,arrays):
        #简单选择排序
        #升序
        if not arrays:
            return
        for i in range(len(arrays)):#从第一个数开始，依次和后面的无序区比较，
            # 直到找到最小值放入有序区的末端为止
            minindex=i
            for j in range(i+1,len(arrays)):
                if arrays[i]>arrays[j]:#如果无序区中的值更小，要更新最小值的索引
                    minindex=j
            arrays[i], arrays[minindex] = arrays[minindex], arrays[i]#将最小值交换到前面有序区
        return arrays
class insert_sort:
    def direct_insert_sort(self,arrays):
        if not arrays:
            return
        for i in range(len(arrays)-1):
            tmp = arrays[i + 1]
            tmpindex=i+1
            for j in range(i+1)[::-1]: #依次与前面的数比较，当比前面的数小的时候，索引前进一位
                if tmp<arrays[j]:
                    tmpindex=tmpindex-1
                else:break
            arrays[tmpindex+1:i+2]=arrays[tmpindex:i+1] #比tmp小的部分数组整体往后挪一位
            arrays[tmpindex]=tmp #将tmp的值插入到对应的索引位置
        return arrays
    def shell_sort(self,arrays):
        totel_l=len(arrays)
        gap=totel_l//2 #首次gap取数组长度的一半
        while gap>=1:  #循环直到间隔gap为1
            for i in range(gap):
                j=0 #表示从i开始的子序列中间隔为gap的数的个数
                while i+j*gap<totel_l:
                    j=j+1 #未到队尾，子序列个数加一
                j=j-1
                #对抽取出来的等间隔子序列做插入排序
                A=arrays[i:i+j*gap+1:gap]
                arrays[i:i+j*gap+1:gap]=\
                    self.direct_insert_sort(arrays[i:i+j*gap+1:gap])
            gap=gap//2 #所有子序列排序结束，间隔gap减半
        return arrays
class merge_sort:
    def merge(self,arrays,leftbound,mid,rightbound):
        if leftbound>=rightbound:
            return
        newlist=[]#创建一个新的列表来放置排序好的数
        i=leftbound
        j=mid+1
        while (i <=mid and j<=rightbound): #i，j,分别表示两组有序序列的指针
            if arrays[i]<=arrays[j]: #哪个指针指向的数值比较小，就排到序列前端
                newlist.append(arrays[i])
                i=i+1
            else:
                newlist.append(arrays[j])
                j=j+1
        if i<=mid:
            newlist.extend(arrays[i:mid+1])
        elif j<=rightbound:
            newlist.extend(arrays[j:rightbound+1])
        arrays[leftbound:rightbound+1]=newlist[:]
        return arrays

    def mergesort(self,arrays,leftbound,rightbound):
        if leftbound==rightbound:
            return arrays
        mid=leftbound+(rightbound-leftbound)//2
        self.mergesort(arrays,leftbound,mid) #左部分排序，递归方法，直到分割的组长度为1的时候返回值
        self.mergesort(arrays,mid+1,rightbound) #对右边部分进行排序
        self.merge(arrays,leftbound,mid,rightbound)#将排序好的左右两部分merge
        return arrays
class calculatenum_sort:
    def calculatesort(self,arrays):
        if not arrays:
            return arrays
        max_a=arrays[0]
        min_a=arrays[0]
        for i in arrays: #找出数组中的最大值和最小值
            if i>max_a:
                max_a=i
            if i<min_a:
                min_a=i
        left=0-min_a  #将最小值与我们countarrays里面的首个索引0对应起来
        countarrays=[0]*(max_a-min_a+1)
        for i in arrays:
            countarrays[i+left]+=1
        k=0
        for j in range(len(countarrays)):
            if countarrays[j]!=0:
                m=countarrays[j]
                arrays[k:k+m]=[j-left]*m #这里记得要把索引恢复成原始的数据，比如索引0对应序列的最小值min
                k=k+m
        return arrays
    def calculatesort1(self,arrays):  #保证数列的稳定性，即相等数字的相对位置关系不变
        if not arrays:
            return arrays
        max_a=arrays[0]
        min_a=arrays[0]
        for i in arrays: #找出数组中的最大值和最小值
            if i>max_a:
                max_a=i
            if i<min_a:
                min_a=i
        left=0-min_a  #将最小值与我们countarrays里面的首个索引0对应起来
        countarrays=[0]*(max_a-min_a+1)
        for i in arrays:
            countarrays[i+left]+=1
        for j in range(1,len(countarrays)):
            countarrays[j]+=countarrays[j-1]  #这一步是使得countarrays里面的数对应这些想等的数在序列中末尾的索引（加一）。
            # 比如从起点开始有3个0，2个1，3+2=5，1右边界对应的下标就是第五个
        result=[0]*len(arrays)
        for k in range(len(arrays))[::-1]: #从最后一位开始遍历，这样对于相等的数，在后面的会优先到后面
            result[countarrays[arrays[k]+left]-1]=arrays[k]
            countarrays[arrays[k]+left]-=1
        return result

class base_sort:
    def basesort(self,arrays):
        if not arrays:
            return arrays
        max_abs=abs(arrays[0])
        for i in arrays[1:]:
            if max_abs<abs(i):
                max_abs=abs(i)  #找出绝对值最大的数
        max_bit=1
        while max_abs//10 >0: #计算出最大的位数
            max_bit+=1
            max_abs=max_abs//10
        for i in range(1,max_bit+1):
            result = [0] * len(arrays)
            countarray = [0] * 10
            for j in arrays:
                nums=(j//(pow(10,i-1)))%10
                countarray[nums]+=1
            for k in range(1,len(countarray)):
                countarray[k]+=countarray[k-1]
            for m in arrays[::-1]:
                nums1=(m//(pow(10,i-1)))%10
                result[countarray[nums1]-1]=m
                countarray[nums1]-=1
            arrays=result[::]
        if arrays[-1]<0 and arrays[0]>=0:
            for l in range(len(arrays))[::-1]:
                if arrays[l]>=0:
                    break
            arrays=arrays[l+1:]+arrays[:l+1]
        return arrays

'''
# arrays = [7,9,8,7,7,-7,7,7,7,7,7,6,5,3,4,3,10,0,-3,8]
# arrays=[]
arrays=[1,2,3,11,100,77,7,8,9]
# arrays=[2,1,3]
# arrays=[234,12,3,5870]
# S=sort_methods()
# print(S.maopao(arrays))
# print(S.fast_sort(arrays,0,len(arrays)-1))
# H=heap_methods()
# print(H.heap_sort(arrays))
# S=select_sort()
# print(S.simple_select_sort(arrays))
# I=insert_sort()
# print(I.direct_insert_sort(arrays))
# print(I.shell_sort(arrays))
# M=merge_sort()
# print(M.mergesort(arrays,0,2))
# C=calculatenum_sort()
# print(C.calculatesort1(arrays))
'''
arrays=eval(input())
I=insert_sort()
print(I.direct_insert_sort(arrays))
