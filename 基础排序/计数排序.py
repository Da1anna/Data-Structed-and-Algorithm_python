'''
计数排序

Description
实现计数排序，通过多次遍历数组，统计比每一个元素小的
其它元素个数，根据该统计量对数据进行排序。

Input
输入的每一行表示一个元素为正整数的数组，
所有值用空格隔开，第一个值为数值长度，其余为数组元素值。

Output
输出的每一行为排序结果，用空格隔开，末尾不要空格。

Sample Input 1
13 24 3 56 34 3 78 12 29 49 84 51 9 100

Sample Output 1
3 3 9 12 24 29 34 49 51 56 78 84 100
'''

def Count_sort(arr):
    maxm = max(arr)
    minm = min(arr)
    B = [0]*(maxm - minm + 1)
    for num in arr:
        B[num - minm] += 1
    # print(B)
    arr.clear()
    for i in range(len(B)):
        while B[i]:
            arr.append(i + minm)
            B[i] -= 1
    return arr

A = list(map(int,input().strip().split()))
res = Count_sort(A)
print(' '.join(str(i) for i in res).strip())















