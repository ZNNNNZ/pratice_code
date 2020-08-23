'''
class Solution:
    def Method(self,n,m):
        if n<=0 or m<=0:
            return
        nums=[[]]
        result=[]
        for i in range(1,n+1):
            length=len(nums)
            j=0
            while j < length:
                tmp=nums[j][:]
                if i not in tmp and len(tmp)<m:
                    tmp.append(i)
                    if len(tmp)==m:
                        result.append(tmp)
                    else:
                        nums.append(tmp)
                j+=1
        nums=[]
        for k in range(len(result)):
            tmp1=result[k]
            ans=''
            while len(tmp1)>=1:
                ans+=str(tmp1.pop(0))
            nums.append(int(ans))
        nums.sort()
        while nums:
            tmp0=str(nums.pop(0))
            ans=''
            for l in range(m-1):
                ans+=tmp0[l]+' '
            ans+=tmp0[l+1:]
            print(ans)

S=Solution()
S.Method(10,2)

import sys
while 1:
    try:
        T=sys.stdin.readline().strip()
        T=int(T)
        nums=[]
        for i in range(T):
            n=sys.stdin.readline().strip()
            n=int(n)
            nums.append(n)
        S = Solution()
        S.Method(nums)
    except:
        break

import sys
while 1:
    try:
        nums=sys.stdin.readline().strip()
        a=[]
        for i in nums.split():
            a.append(int(i))
        S = Solution()
        S.Method(a[0],a[1])
    except:
        break
'''
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head=ListNode(0)
        ans=head
        pre=0
        while l1 or l2:
            if l1:tmp1=l1.val
            else:tmp1=0
            if l2:tmp2=l2.val
            else:tmp2=0
            tmp=tmp1+tmp2+pre
            pre=tmp//10
            ans.val=tmp%10
            ans.next=ListNode(0)
            ans=ans.next
            l1=l1.next
            l2=l2.next
        ans=None
        return head
S=Solution()
l1=ListNode(1)
l1.next=ListNode(2)
l2=ListNode(9)
print(S.addTwoNumbers(l1,l2))
'''
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dicts={}
        i=0
        count=0
        max_count=0
        while i <len(s):
            if s[i] not in dicts:
                dicts[s[i]]=i
                count+=1
                i+=1
            else:
                max_count=max(max_count,count)
                count=0
                i=dicts[s[i]]+1
                dicts={}
        return max(max_count,count)
s='bbsc'
S=Solution()
print(S.lengthOfLongestSubstring(s))
'''
'''
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if not image or not image[0]:
            return image
        iniColor=image[sr][sc]
        if iniColor==newColor:
            return image
        def helper(sr,sc,image,iniColor,newColor):
            if sr<0 or sr>len(image) or sc<0 or sc>len(image[0]):
                return
            if image[sr][sc]==iniColor:
                image[sr][sc] =newColor
                helper(sr,sc,image,iniColor,newColor)
            if sr>0 and image[sr-1][sc]==iniColor:
                image[sr-1][sc]=newColor
                helper(sr-1,sc,image,iniColor,newColor)
            if sc>0 and image[sr][sc-1]==iniColor:
                image[sr][sc-1]=newColor
                helper(sr,sc-1,image,iniColor,newColor)
            if sr<len(image)-1 and image[sr+1][sc]==iniColor:
                image[sr+1][sc]=newColor
                helper(sr+1,sc,image,iniColor,newColor)
            if sc<len(image[0])-1 and image[sr][sc+1]==iniColor:
                image[sr][sc+1]=newColor
                helper(sr,sc+1,image,iniColor,newColor)
            return
        helper(sr,sc,image,iniColor,newColor)
        return image
S=Solution()
print(S.floodFill([[0,0,0],[0,1,0]],1,1,1))
'''
'''
class Solution(object): #leetcode5,不算是最优算法，时间复杂度O(N^2)
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s)==1:
            return s
        def helper(left,right,s):
            ans=''
            while left>=0 and right<len(s) and left<=right:
                if s[left]==s[right]:
                    ans=s[left:right+1]
                    left-=1
                    right+=1
                else:break
            return ans
        max_str=''
        for i in range(len(s)-1):
            str1=helper(i,i,s)
            if len(str1)>len(max_str):
                max_str=str1
            str2=helper(i,i+1,s)
            if len(str2)>len(max_str):
                max_str=str2
        return max_str
S=Solution()
print(S.longestPalindrome('dbba'))
'''

