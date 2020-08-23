'''
def InttoStr(nums):
    if type(nums) is int:
        nums=str(nums)
        return nums
    elif type(nums) is dict:
        for i in nums:
            nums[i]=InttoStr(nums[i])
    elif type(nums) is list:
        for j in range(len(nums)):
            nums[j]=InttoStr(nums[j])
    elif type(nums) is tuple:
        nums=list(nums)
        for k in range(len(nums)):
            nums[k]=InttoStr(nums[k])
        nums=tuple(nums)
    return nums

nums=[1,2,{'2':3}]
print(InttoStr(nums))
'''

'''
class Solution:
    def MaxLength(self,n):
        a=n//3
        b=n%3
        if b==0:
            return pow(3,a)
        elif b==1:
            return pow(3,a-1)*4
        elif b==2:
            return pow(3,a)*2

S=Solution()
print(S.MaxLength(5))
'''
'''
class Solution:
    def FindMethod(self,n,nums,number):
        def helper(nums,number,left,right):
            if left==right and nums[left]==number:
                return left
            elif left>=right:
                return -1
            mid=left+(right-left)//2
            if nums[left]<=number and nums[mid]>=number:
                right=mid
            else:
                left=mid+1
            return helper(nums,number,left,right)
        return helper(nums,number,0,n-1)

S=Solution()
nums=[19,21]
print(S.FindMethod(2,nums,19))
'''
'''
class Solution:
    def IsPossible(self,n):
        nums=[]
        a=n
        while a:
            nums.insert(0,a%10)
            a=a//10
        for i in range(2,10):
            b=n*i
            tmp=nums[:]
            while b:
                tmp_num=b%10
                if tmp_num in tmp:
                    tmp.pop(tmp.index(tmp_num))
                    b=b//10
                else:
                    break
            if not tmp:return 'Possible'
        return 'Impossible'
S=Solution()
print(S.IsPossible(135))
import sys
while 1:
    try:
        n=sys.stdin.readline().split()
        n=int(n[0])
        S=Solution()
        for i in range(n):
            a=sys.stdin.readline().split()
            print(S.IsPossible(int(a[0])))
    except:
        break
'''

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        lengthx=len(board)
        lengthy=len(board[0])
        location=[[0 for i in range(lengthy)] for j in range(lengthx)]
        def helper(board,location,x,y):
            if x<0 or y<0 or x>=len(board) or y>=len(board[0]):
                return
            # if x>0 and x < len(board)-2 and y>0 and y<len(board[0])-2 \
            #         and board[x-1][y]=='X' and board[x+1][y]=='X'\
            #         and board[x][y+1]=='X' and board[x][y-1]=='X':
            #     return
            if x>0 and board[x-1][y]=='O' and location[x-1][y]==0:
                location[x-1][y]=1
                helper(board,location,x-1,y)
            if x<len(board)-1 and board[x+1][y]=='O' and location[x+1][y]==0:
                location[x+1][y]=1
                helper(board, location, x + 1, y)
            if y<len(board[0])-1 and board[x][y+1]=='O' and location[x][y+1]==0:
                location[x][y+1]=1
                helper(board, location, x, y+1)
            if y>0 and board[x][y-1]=='O' and location[x][y-1]==0:
                location[x][y - 1] = 1
                helper(board, location, x, y - 1)
            return

        for i in range(lengthy):
            if board[0][i]=='O' and location[0][i]==0:
                location[0][i]=1
                helper(board,location,0,i)
            if board[lengthx-1][i]=='O'\
                    and location[lengthx-1][i]==0:
                location[lengthx-1][i]=1
                helper(board, location,lengthx-1,i)
        for j in range(lengthx):
            if board[j][0]=='O' and location[j][0]==0:
                location[j][0]=1
                helper(board, location, j, 0)
            if board[j][lengthy-1]=='O'\
                    and location[j][lengthy-1]==0:
                location[j][lengthy-1]=1
                helper(board, location, j, lengthy-1)
        for k in range(1,lengthx-1):
            for m in range(1,lengthy-1):
                if board[k][m]=='O' and location[k][m]==0:
                    board[k][m]='X'

S=Solution()
# board=[]
# board.append(list('XXXX'))
# board.append(list('XOXO'))
# board.append(list('XOOX'))
# board.append(list('XXXX'))
board=[["X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X"],
       ["X","X","X","X","X","X","X","X","X","O","O","O","X","X","X","X","X","X","X","X"],
       ["X","X","X","X","X","O","O","O","X","O","X","O","X","X","X","X","X","X","X","X"],
       ["X","X","X","X","X","O","X","O","X","O","X","O","O","O","X","X","X","X","X","X"],
       ["X","X","X","X","X","O","X","O","O","O","X","X","X","X","X","X","X","X","X","X"],
       ["X","X","X","X","X","O","X","X","X","X","X","X","X","X","X","X","X","X","X","X"]]
S.solve(board)
print(board)



