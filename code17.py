'''
n个城市n个人，每个城市一个人，选择一个城市x，所有人去那聚会，聚合结束所有人返回各自城市。
有m条单向路径，保证每个人可以到达城市x，一个人所消耗时间为往返时间和，
每个人选择自己的最短路径，问最长的时间是多少。
**输入：**第一行：n个城市，m个单向路数量，x是参加聚会的城市 4 8 2
后面m行：单向路起点 终点 花费的时间1 2 4；1 3 2；1 4 7；2 1 1；2 3 5；3 1 2；3 4 4；4 2 3；
**输出：**花费时间最多的是多少 10（4到2 的时间为3；2回到4的时间是7：所以答案是10）
'''
class Solution():
    def timemax(self,n,m,x,arrays):
        #读取城市之间的路程表
        distance=[[0]*n for i in range(n)]
        for j in arrays:
            distance[j[0]-1][j[1]-1]=j[2]
        #计算两个城市往返的最短路径
        for k in range(n):
            for m in range(n):
                for p in range(n):
                    if distance[m][p]>0 and distance[m][k]>0 and distance[k][p]>0:
                        if distance[m][p]>(distance[m][k]+distance[k][p]):
                            distance[m][p] = (distance[m][k] + distance[k][p])
                    elif distance[m][p]==0 and (distance[m][k]>0 and distance[k][p]>0):
                        distance[m][p] = (distance[m][k] + distance[k][p])
        #计算其他城市到达目的地的最长距离
        maxd = distance[0][x - 1] + distance[x - 1][0]
        for q in range(1,n):
            if maxd<distance[q][x - 1]+distance[x-1][q]:
                maxd=distance[q][x - 1]+distance[x-1][q]
        return maxd

S=Solution()
arrays=[[1,2,4],[1,3,2],[1,4,7],[2,1,1],[2,3,5],[3,1,2],[3,4,4],[4,2,3],[5,2,7],[1,5,10],[5,4,1]]
print(S.timemax(5,11,2,arrays))
