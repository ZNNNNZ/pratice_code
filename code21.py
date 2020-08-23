'''
大数乘法
大数指超过int64_t 可承载范围的数字

输入描述:
输入两行数n1, n2 (0 < n* < 2^100)

输出描述:
输出两数之积

输入例子1:
2
3

输出例子1:
6

输入例子2:
9223372024429430685
34223371424429430685

输出例子2:
315654886577740006976078312593219569225
'''
class Solution:
    def mul_longnums(self,n1,n2):
        len1=len(n1)
        len2=len(n2)
        new_list=[0]*(len1+len2)
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                s1=int(n1[i-1])
                s2=int(n2[j - 1])
                new_list[i+j-1]+=s1*s2
        for k in range(1,len(new_list))[::-1]:
            if new_list[k]>=10:
                new_list[k-1]+=new_list[k]//10
                new_list[k]=new_list[k]%10
        m=0
        while new_list[m]==0:
            m=m+1
        for q in range(m,len(new_list)):
            print(new_list[q],end='')
S=Solution()
input1=input('输入第一个大数：')
input2=input('输入第二个大数：')
S.mul_longnums(input1,input2)



