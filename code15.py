'''
删除一组字符中重复的元素，例如aaaaab删除后为b。
输入是多组字符，输出是每一行删除后的元素。若全部删除则输出no
例输入：a
       aaaabbb
输出：a
     no
'''
# a=[1,2,3.4,'hello','hello','world',[],(1),{3},'hello']
# print(a[::-1])
# b=a.index([])
# c=a.count('hello')
# d=(a,9,0)
# print(d[0][4])
# a.clear()
# print(a)
# a=[1,2,3]
# a.insert(0,'hhh')
# a=[1,4,3,6,7]
# b=a.pop(2)
# print(a,b)
# a=[1,4,3,6,7]
# b=a.remove(6)
# print(a,b)
# dic={}
# name=input('请输入姓名：')
# dic.update(name=name)
# age=int(input('请输入年龄：'))
# dic.update(age=age)
# sex=input('请输入性别：')
# dic.update(sex=sex)
# b=dic.get("age")
# print(dic,b)
'''
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b
'''
'''
浅拷贝
list=[[1,3],[4,2],1]
# list1=list
##copy函数
# list1=list.copy()
##列表生成式
# list1=[i for i in list]
##循环遍历式
# list1=[]
# for i in range(len(list)):
#     list1.append(list[i])
##切片式
list1=list[:]
list[1][0]=10
'''
'''
# 深拷贝
import copy
list=[[1,3],[4,2],1]
list1=copy.deepcopy(list)
list[0][1]=10
print("list:",list)
print("list1:",list1)
'''
'''
dict2={(1,2):'jjjj'}
a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]
zipped = zip(a,c)     # 打包为元组的列表
print(list(zipped))
'''
list = []
for i in range(3):
    def test(x): print(x + i)
    list.append(test)
for num in list:
    num(2)