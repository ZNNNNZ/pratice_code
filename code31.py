'''
class Solution():
    def change_s(self,strings):
        if not strings or len(strings)>10:return
        for k in strings:
            if k not in 'RGBY':
                return
        i=0
        j=1
        num=0
        while j <=(len(strings)-1):
            if strings[i]==strings[j]:
                num+=1
                i=i+2
                j=j+2
            else:
                i=i+1
                j=j+1
        return num

while True:
    try:
        S=Solution()
        strings=input()
        print(S.change_s(strings))
    except:
        break
'''
'''
class Solution():
    def max_strings(self,strings):
        if len(strings)<=2 or len(strings)%2==1:return 0
        i = len(strings) // 2 - 1
        length=len(strings)
        while i>=0:
            strings=strings[:length-2]
            length-=2
            i = len(strings) // 2 - 1
            j = len(strings) // 2
            m=j
            k=0
            while k<=i:
                if strings[k]==strings[m]:
                    k=k+1
                    m=m+1
                else:break
            if k-1==i:return length
        return length
while True:
    try:
        S=Solution()
        strings=input()
        print(S.max_strings(strings))
    except:
        break
'''
class Solution():
    def min_huiwen(self,strings):
        count=[0]*26
        nums1=0
        for i in strings:
            num=ord(i)-97
            count[num]+=1
        for j in range(26):
            if count[j]>0:
                if count[j]%2==1:
                    nums1+=1
        if nums1>0:
            return nums1
        else:return 1

while True:
    try:
        S=Solution()
        strings=input()
        print(S.min_huiwen(strings))
    except:
        break
