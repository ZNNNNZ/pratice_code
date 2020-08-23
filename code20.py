'''
给定一个字符串 S，如果 S 满足以下要求中的任意一个则返回 true，否则返回 false:
1. 全部都是大写字母，比如 "BILIBILI"
2. 全部都是小写字母，比如 "bilibili"
3. 首字母大写，比如 "Bilibili"
输入描述:
输入为字符串，且只包含英文字母。
输出描述:
输出为 true 或则 false
输入例子1:
bilibili
输出例子1:
true
输入例子2:
BiliBili
输出例子2:
false
'''
class Solution:
    def istrue(self,strings):
        if not strings:
            return 'false'
        if len(strings)==1 and ord(strings[0])>=65 and ord(strings[0])<=122:
            return 'true'
        flag='false'
        ini=strings[0]
        sec=strings[1]
        if (ord(ini)>=65 and ord(ini)<=90)\
            and (ord(sec)>=65 and ord(sec)<=90):
            flag = 'true'
            for i in strings[2:]:
                if ord(i)<65 or ord(i)>90:
                    flag = 'false'
                    break

        if ((ord(ini) >= 65 and ord(ini) <= 90) or (ord(ini) >= 97 and ord(ini) <= 122)) \
                and (ord(sec) >= 97 and ord(sec) <= 122):
            flag = 'true'
            for i in strings[2:]:
                if ord(i) < 97 or ord(i) > 122:
                    flag = 'false'
                    break
        return flag

S=Solution()
strings=input()
print(S.istrue(strings))
