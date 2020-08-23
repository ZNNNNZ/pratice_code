'''
class Solution:
    def MaxNum(self,n,nums):
        if n<=0:
            return 0
        count=0
        for i in range(len(nums)):
            if nums[i]>1 and nums[i]<=3:
                count+=1
            elif nums[i]>=4:
                count+=nums[i]//2
        return count
# S=Solution()
# print(S.MaxNum(3,[1,1,1]))

import sys
while 1:
    try:
        S=Solution()
        n=sys.stdin.readline().strip()
        n=int(n)
        str=sys.stdin.readline().strip()
        values = list(map(int, str.split()))
        print(S.MaxNum(n,values))
    except:
        break
'''


class Solution:
    def __init__(self,n):
        self.mem=[0]*(n-1)
    def MinTime(self,n,a,b):
        if n<=0:
            return '08:00:00 am'
        hour=8
        min=0
        sec=0
        def helper(k,a,b):
            if k<0 and len(a)%2==0:return 0
            if k < 0 and len(a) % 2 == 1: return a[0]
            if self.mem[k]!=0:
                return self.mem[k]
            tmp1=a[k+1]
            tmp2=b[k]
            if tmp1+helper(k-1,a,b)<=(tmp2+helper(k-2,a,b)):
                self.mem[k]=tmp1+helper(k-1,a,b)
                return tmp1+helper(k-1,a,b)
            else:
                self.mem[k] = tmp2 + helper(k - 2, a, b)
                return tmp2 + helper(k - 2, a, b)
        times=helper(len(b)-1,a,b)
        sec += times%60
        min += times//60
        hour += min //60
        min = min%60
        if hour>12:
            hour-=12
            tail=' pm'
        else:
            tail=' am'
        headh = ''
        if hour<10:headh='0'
        headmin=':'
        if min<10:headmin=':0'
        headsec=':'
        if sec<10:headsec=':0'
        return headh+str(hour)+headmin+str(min)+headsec+str(sec)+tail
S=Solution(6)
print(S.MinTime(6,[2,30,45,4,30,55],[20,15,3,56,70]))
# import sys
# while 1:
#     try:
#         T=sys.stdin.readline().strip()
#         T=int(T)
#         for i in range(T):
#             n=sys.stdin.readline().strip()
#             n=int(n)
#             if n==1:
#                 stra = sys.stdin.readline().strip()
#                 a = list(map(int, stra.split()))
#                 S = Solution(n)
#                 print(S.MinTime(n, a, []))
#             else:
#                 stra=sys.stdin.readline().strip()
#                 a = list(map(int, stra.split()))
#                 strb = sys.stdin.readline().strip()
#                 b = list(map(int, strb.split()))
#                 S = Solution(n)
#                 print(S.MinTime(n,a,b))
#     except:
#         break



'''

class Solution:
    def MinNum(self,n,nums):
        nums.sort()
        totel_num=sum(nums)
        mid_num=totel_num//2
        i=len(nums)//2+1
        count=0
'''



