'''
class Solution:
    def max_kouzhao(self,N):
        if N<=1 or N>=15:return
        num=[5,3,3,2,4,1]
        prices=[1,2,2,2,5,3]
        nums=0
        price=0
        for i in range(len(num)):
            if price>N:
                nums=nums-num[i-1]
                break
            elif N-price==5 and i>2:
                nums+=4
                break
            else:
                price+=prices[i]
                nums+=num[i]
        return nums

while True:
    try:
        S=Solution()
        N=int(input())
        print(S.max_kouzhao(N))
    except:
        break
'''
class Solution:
    def is_equal(self,arrs):
        if not arrs:return
        l1=sum(arrs[0:4])
        l2=sum(arrs[3:7])
        l3=arrs[0]+sum(arrs[6:])
        if l1==l2 and l2==l3:
            return 'yes'
        else:
            return 'no'

while True:
    try:
        S=Solution()
        Num=list(eval(input()))
        print(S.is_equal(Num))
    except:
        break