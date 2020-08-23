'''
输入描述:
输入一行字串（不会为空）
ABAKJSDYUIWNQJNDSAHDBALSDH
输入一个字符集（不会为空，也不会出现重复字符）
ABD

输出描述:
输出包含了字符集所有字符的第一个最小子串，例如上面的输入对应输出DBA
如果没有符合条件的子串，则输出#

输入例子1:
ABAKJSDYUIWNQJNDSAHDBALSDH
ABD

输出例子1:
DBA
'''
class bilibili_s:
    def find_minstr(self,nums,strings):
        length=len(strings)
        minstr = []
        for i in range(len(nums)-length+1):
            for j in nums[i:i+length]:
                if j not in strings or j in minstr:
                    minstr = []
                    break
                elif (not minstr) or j not in minstr:
                    minstr.append(j)
            if len(minstr)==length:
                break
            else:minstr = []
        if not minstr:return '#'
        else:
            k=minstr[0]
            for m in minstr[1:]:
                k=k+m
            return k
'''
S=bilibili_s()
input1=input('请输入字符串：')
inout2=input('请输入字符集：')
print(S.find_minstr(input1,inout2))
'''
while True:
    try:
        lines1=input()
        lines2=input()
        S=bilibili_s()
        print(S.find_minstr(lines1,lines2))
    except Exception as e:
        print ('报错信息：',e)
        break