#题目描述：将输入字符串的空格“ ”替换为“%20”
# -*- coding:utf-8 -*-
# class Solution:
#     # s 源字符串
#     def replaceSpace(self, s):
#         # write code here
#         if " " in s:
#             n = len(s)
#             for i in range(n):
#                 if s[i] == " ":
#                     s=s[:i]+"%20"+s[i+1:]
#             print(s)
#             # print(type(s))
#
#         else:
#             print(s)
#
# S = Solution()
# s = input()
# S.replaceSpace(s)
#
# # s=1234
# # s=str(s)
# # print(s)
# # print(type(s))

class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        if ' ' in s:
            n = len(s)
            s = list(s)
            for i in range(n):
                if s[i] == ' ':
                    s[i] = '%20'
            return  ''.join(s)

        else:
            return s


S = Solution()
s = input()
print(S.replaceSpace(s))
print(type(S.replaceSpace(s)))