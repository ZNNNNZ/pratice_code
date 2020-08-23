'''
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        nums=[]
        for x in s.split():
            nums.append(x)
        result=''
        for i in range(1,len(nums))[::-1]:
            result+=nums[i]
            result+=' '
        if nums:
            result+=nums[0]
        return result

S=Solution()
print(S.reverseWords(''))
'''

'''
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack=[]
        tmp=''
        for i in range(len(path)):
            if tmp:
                if path[i]=='/':
                    if tmp!='..' and tmp!='.':
                        stack.append(tmp)
                    elif tmp=='..' and stack:
                        stack.pop()
                    tmp=''
                else:
                    tmp+=path[i]
            elif path[i]!='/':
                tmp+=path[i]
        if tmp:
            if tmp!='.' and tmp!='..':
                stack.append(tmp)
            elif tmp=='..' and stack:
                stack.pop()
        path='/'
        for j in stack:
            if path[-1] != '/':
                path += '/'
            path+=j
        return path

S=Solution()
strs='/a/home/'
print(S.simplifyPath(strs))
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left=0
        right=len(nums)-1
        mid=left+(right-left)//2
        for i in range(1,len(nums)):
            res=nums[i]-nums[i-1]
            if res<0:
                mid=i-1
        while left<right:
            if target==nums[left]:
                return left
            elif target==nums[right]:
                return right
            elif target==nums[mid]:
                return mid
            elif target>nums[left] and target<nums[mid]:
                right=mid-1
            else:
                left=mid+1
            mid=left+(right-left)//2
        if left==right and nums[left]==target:
            return left
        return -1
S=Solution()
nums=[3,4,0,1,2]
print(S.search([],5))