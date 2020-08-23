'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
示例 1:
输入: 123
输出: 321
 示例 2:
输入: -123
输出: -321
示例 3:
输入: 120
输出: 21
注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。
请根据这个假设，如果反转后整数溢出那么就返回 0。
'''
class Solution(object):
    def reverse1(self, x):
        """
        :type x: int
        :rtype: int
        """
        res=0
        max_val=pow(2,31)-1
        min_val=-pow(2,31)
        while x:
            if x<0:
                a=abs(x)%10
                pop=-a
            else:
                pop=x%10
            if res>max_val//10 or (res==max_val//10 and pop>max_val%10):
                return 0
            if res<min_val//10 or (res==min_val//10 and pop<-max_val%10-1):
                return 0
            res=res*10+pop
            x=int(x/10)
        return res

    def reverse(self, x):
        max_val=pow(2,31)-1
        min_val=-pow(2,31)
        x=list(str(x))
        if x[0]=='-':
            i=1
        else:
            i=0
        j=len(x)-1
        while i<j:
            x[i],x[j]=x[j],x[i]
            i+=1
            j-=1
        ans=x[0]
        for i in range(1,len(x)):
            ans=ans+x[i]
        if int(ans)>max_val or int(ans)<min_val:
            return 0
        return int(ans)


S=Solution()
print(S.reverse(-123))
