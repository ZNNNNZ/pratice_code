'''
class Solution:
    def Max_count(self,n,nums):
        if n<=3:
            return -1
        tmp_dicts={}
        for i in nums:
            if i not in tmp_dicts:
                tmp_dicts[i]=1
            else:
                tmp_dicts[i]+=1
        a=0
        for j in tmp_dicts:
            if tmp_dicts[j]>=2:
                a=max(a,j)
        if a==0:return -1
        tmp_dicts[a]=0
        b=0
        for k in tmp_dicts:
            if tmp_dicts[k]>=2:
                b=max(b,k)
        if b==0:return -1
        return a*b
'''

'''
class Solution:
    def Min_count(self,n,nums):
        if n<=1:
            return 0
        count=0
        res=0
        for i in range(1,n):
            res+=nums[i]-nums[i-1]
            if res<0:
                count+=1
        return count

while 1:
    n=input()
    s=input()
    nums=[]
    if n!='':
        for x in s.split():
            nums.append(int(x))
        n=int(n)
        S=Solution()
        print(S.Min_count(n,nums))
    else:
        break
'''
class Solution:
    def Min_count(self,nums1,arrs):
        y=nums1[1]
        count=0
        for i in range(1,nums1[0]):
            res=arrs[i][0]-arrs[i-1][0]
            if res<=2*y:
                count+=max(arrs[i][1],arrs[i-1][1])
                arrs[i][1]=0
                arrs[i - 1][1]=0
            else:
                count+=arrs[i - 1][1]
        if arrs[nums1[0] - 1][1]!=0:
            count += arrs[nums1[0] - 1][1]
        return count

while 1:
    n=input()
    if n != '':
        nums1=[]
        for j in n.split():
            nums1.append(int(j))
        arrs=[]
        for i in range(nums1[0]):
            s = input()
            nums = []
            for x in s.split():
                nums.append(int(x))
            arrs.append(nums)
        S=Solution()
        print(S.Min_count(nums1,arrs))
    else:
        break

