'''
给定一个字符串

{xxx[xxx{xxx}]xx{x[xxx]xxx{xxx}xx}x}

判断其中的 {}[]() 是否成对出现

成对出现输出True,未成对出现输出False
在这里我们用栈的方法来实现
'''
class Stack():
    def __init__(self):
        self._data=[]
    def push(self,data):
        self._data.append(data)
    def pop(self):
        return self._data.pop()
    def get_size(self):
        return len(self._data)

class Match():
    def ismatch(self,strings):
        S=Stack()
        flag=0
        for i in strings:
            if i in '{[(':
                S.push(i)
                flag=1
            elif i in '}])':
                if S.get_size()==0:return False
                else:S.pop()
        if S.get_size()==0 and flag==1:
            return True
        else:
            return False
# while True:
#     try:
#         strings=input()
#         M=Match()
#         print(M.ismatch(strings))
#     except:
#         break

'''
定义队列
'''
class Duilie():
    def __init__(self):
        self._data1 =[]
    def push(self,item):
        self._data1.append(item)
    def pop(self):
        self._data1.remove(self._data1[0])
        return self._data1
    def get_lines(self):
        return self._data1


# try:
#     D=Duilie()
#     D.push(1)
#     D.push(2)
#     D.push(3)
#     print(D.get_lines())
#     D.pop()
#     D.pop()
#     print(D.get_lines())
# except:
#     print('over')
'''
定义链表
'''
#链表
class  Linknode():
    def __init__(self,data=None):
        self.data=data
        self.next=None
    #往链表尾部添加新节点
    def link_append(self,data):
        item=self
        while item.next is not None:
            item=item.next
        item.next=Linknode(data)
        return item.next
    #遍历链表
    def link_travel(self):
        item=self
        list1=[]
        while item is not None:
            list1.append(item.data)
            item=item.next
        return list1
    #查找表中数据
    def link_search(self,data):
        item = self
        index=0
        while item is not None:
            if item.data==data:
                return index
            else:
                index+=1
                item=item.next
        return -1
    #在表中插入数据
    def link_insert(self,pos,data):
        item=self
        index=0
        #如果输入的pos不符合规范
        if pos<=0:print('error:the pos <=0')
        while item.next is not None:
            if index==pos-1:
                tmp=Linknode(data)
                tmp.next=item.next
                item.next=tmp
                return item
            else:
                index+=1
                item=item.next
        #如果pos超过链表范围，则直接添加在链表末尾
        if index<pos:
            tmp = Linknode(data)
            item.next = tmp
            return item

class Link_operation():
    #添加头结点
    def __init__(self,data):
        self.head=Linknode(data)
    #在链表尾部添加新的节点
    def link_append(self,data):
        self.head.link_append(data)
    #遍历并打印链表
    def travel(self):
        print(self.head.link_travel())
    def search(self,data):
        print(self.head.link_search(data))
    def insert(self,pos,data):
        self.head.link_insert(pos,data)
        self.travel()

# L=Link_operation(1)
# for i in range(3):
#     data=int(input())
#     L.link_append(data)
# L.travel()
# L.insert(10,100)
# L.search(100)

'''
定义树
'''
class Btree():
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None
    #设定根节点
    def setup(self,data):
        self.tree=Btree(data)
        self.list=[]
    #创建树
    def create_Btree(self):
        self.tree.left=Btree(1)
        self.tree.right = Btree(2)
        self.tree.left.left = Btree(3)
        self.tree.left.right = Btree(4)
        self.tree.right.left = Btree(5)
        self.tree.right.right = Btree(6)
    def travel_tree(self,tree,order='front'):
        if order == 'front':
            if tree is None:
                return
            # print(tree.data)      #先序遍历
            self.list.append(tree.data)
            self.travel_tree(tree.left)
            self.travel_tree(tree.right)
        elif order == 'mid':
            if tree is None:
                return
            self.travel_tree(tree.left,order='mid')
            # print(tree.data)   #中序遍历
            self.list.append(tree.data)
            self.travel_tree(tree.right,order='mid')
        elif order == 'rear':
            if tree is None:
                return
            self.travel_tree(tree.left,order='rear')
            self.travel_tree(tree.right,order='rear')
            # print(tree.data)      #后序遍历
            self.list.append(tree.data)
    def TreeDepth(self, pRoot):
        if pRoot is None:
            return 0
        return max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1

        # 广度遍历方法（BFS）
    def max_depth(self, root):
            if root is None: return 0
            gen = [root]
            res = 0
            while gen:
                tmp = []
                for node in gen:
                    if node.left: tmp.append(node.left)
                    if node.right: tmp.append(node.right)
                gen = tmp
                res += 1
            return res


B=Btree()
B.setup(0)
B.create_Btree()
B.travel_tree(B.tree,'mid')
print(B.list)
print(B.max_depth(B.tree))
# assert B.TreeDepth(B.tree) == 4, 'false!'
# print(eval(input()))

