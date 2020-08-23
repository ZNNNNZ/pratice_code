'''
class Solution:
    def CountNum(self,n):
        if n<1 or n>pow(10,100):
            return 0
        count=0
        while n>1:
            if n%2==0:
                n=n//2
            else:
                n=n+1
            count+=1
        return count

import sys
for line in sys.stdin:
    a = line.split()
    S=Solution()
    print(S.CountNum(int(a[0])))
'''


class Solution:
    def SubS(self, nums):
        if not nums:
            return nums
        res0 = [[]]
        res0.append([nums[0]])
        for i in range(1, len(nums)):
            L = len(res0)
            for j in range(L):
                tmp1 = res0[j][:]
                tmp1.append(nums[i])
                res0.append(tmp1)
        return res0


S = Solution()
nums = [1, 2, 3]
print(S.SubS(nums))
