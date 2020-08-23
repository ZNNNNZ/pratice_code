'''
# 容器装水、地形盛水问题（二维）
**题目：**给定一个二维数组，数组内对应位置的数值表示该位置的高度，一
个有高低起伏的数组可以装水，问这个二维数组可以装多少水？
'''
class TrapWater:
    class Node:
        def __init__(self,v,i,j):
            self.value=v
            self.row=i
            self.col=j

    def __init__(self):
        self.heap=[]
    # 创建小根堆
    def min_heap(self,node):
        if not self.heap:
            self.heap.append(node)

    def trapwater(self,arrs):
        if not arrs or not arrs[0]:return 0
        m=len(arrs)  #行数
        n=len(arrs[0])  #列数
        isEnter=[[False]*n]*m    #bool值判断每个位置的数是否入堆，False表示没有入堆，True表示入堆




