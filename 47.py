class Solution:
    def MinStrings(self,str):
        if not str or len(str)==1:
            return str
        i=0
        j=len(str)-1
        while i<j:
            tmp1=str[i]
            tmp2=str[j]
            if tmp1==tmp2:
                i+=1
                j-=1
            else:
                i+=1
        if i>=j:
            if i==len(str)-1-j:
                return str
            else:
                m=i+j+1-len(str)
                for k in range(m)[::-1]:
                    str+=str[k]
                return str
        elif i==j and j==len(str)-1:
            length=len(str)
            for k in range(length)[::-1]:
                str+=str[k]
            return str
S=Solution()
print(S.MinStrings('levell'))
# import sys
# while 1:
#     try:
#         S=Solution()
#         str=sys.stdin.readline().split()
#         print(S.MinStrings(str[0]))
#     except:
#         break
