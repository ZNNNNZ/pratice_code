#问题描述——给出一个正整数N和长度L，找出一段长度大于等于L的连续非负整数，他们的和恰好为N。答案可能有多个，我我们需要找出长度最小的那个。
#例如 N = 18 L = 2：
# 5 + 6 + 7 = 18
# 3 + 4 + 5 + 6 = 18
# 都是满足要求的，但是我们输出更短的 5 6 7
# 输入数据包括一行： 两个正整数N(1 ≤ N ≤ 1000000000),L(2 ≤ L ≤ 100)
import math
class Find_num:
    def find_array(self,N,L):
        n=N//2
        i=1
        length_num=[]
        i_num=[]
        while i<=n:
            for length in range(L,10+1):
                sum0=length*i+(length*(length-1)//2)
                # sum_list.append(sum0)
                if sum0==N:
                    length_num.append(length)
                    i_num.append(i)
            i=i+1
        if i_num==[]:
            print('No')
        else:
            length_num.sort()
            i_num.sort(reverse=True)
            for j in range(length_num[0]-1):
                print(i_num[0]+j,end=" ")
            print(int(i_num[0] + j + 1))

    def find_array1(self,N,L):
        i = L
        flag=0
        while i <= 100:
            for length in range(1, N//2+1):
                sum0 = i * length + (i * (i - 1) // 2)
                # sum_list.append(sum0)
                if sum0 == N:
                    flag=1
                    for j in range(i-1):
                        print(length+j,end=" ")
                    print(int(length + j + 1))
                    break
            if flag==1:
                break
            i = i + 1
        if i == 101:
            print('No')

    def find_array2(self,N,L):
        i=L
        while i <=100:
            a1=(2*N-i*(i-1))/(2*i)
            if math.floor(a1)==a1:
                for j in range(i-1):
                    print(int(a1+j),end=" ")
                print(int(a1+j+1))
                break
            i=i+1
        if i==101:
            print('No')

model=Find_num()
N,L=list(map(int, input().split()))
model.find_array1(N,L)
