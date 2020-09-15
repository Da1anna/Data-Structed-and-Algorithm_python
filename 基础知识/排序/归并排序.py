'''
归并排序
这里的代码是二路归并，将两个有序的数组进行归并
有关归并排序的思想、时空复杂度以及推导过程详见博客
https://www.jianshu.com/p/3ad5373465fd
'''
'''
递归版
'''
def Merge_sort(seq):
    '''
    递归函数，用于将序列划分为“有序”的子序列
    :param seq: 待排序序列
    :return: 排好序的序列
    '''
    if len(seq) == 1:
        return seq
    mid = len(seq) // 2     #表示划分位置
    left_seq = Merge_sort(seq[:mid])    #左闭右开
    right_seq = Merge_sort(seq[mid:])   #同上
    return merge2(left_seq,right_seq)

def merge1(seq1,seq2):
    '''
    用于将有序的子序列排序成一个序列
    :param seq1:
    :param seq2:
    :return: sorted single_seq
    '''
    lst = []
    while seq1 and seq2:
        lst.append(seq1.pop(0) if seq1[0] < seq2[0] else seq2.pop(0))
    lst.extend(seq1 if seq1 else seq2)
    return lst
def merge2(seq1,seq2):
    '''
    方法二没有使用python自带的pop功能，考虑到效率不高
    原因：数组pop一个值后，后面的值必将向前移位
    '''
    lst = []
    i,j = 0,0
    while i < len(seq1) and j < len(seq2):
        if seq1[i] < seq2[j]:
            lst.append(seq1[i])
            i += 1
        else:
            lst.append(seq2[j])
            j += 1
    lst.extend(seq1[i:] if i < len(seq1) else seq2[j:])
    return lst



'''
非递归版
'''
def Merge_sort_NotR(arr):
    i = 1
    while  i < len(arr):
        low = 0
        while low < len(arr):
            mid = low + i
            # 因为python切片对于超出索引时会自动处理只选取有效索引部分，故不必担心
            high = mid + i
            merge3(low,mid,high,arr)
            low = high
        i *=2
    return arr

def merge3(low,mid,high,arr):
    '''
    这里的子排序函数的参数与上面两个不同
    原因是迭代与递归的思想不一样，如果也返回排好序的子序列，不好处理迭代
    具体原因以后再分析
    :param arr: 初始输入数组，但每迭代一次都更加有序
    '''
    seq1 = arr[low:mid]
    seq2 = arr[mid:high]
    lst = []
    i,j = 0,0
    while i < len(seq1) and j < len(seq2):
        if seq1[i] < seq2[j]:
            lst.append(seq1[i])
            i += 1
        else:
            lst.append(seq2[j])
            j += 1
    '''
    多一次extend操作，少一次条件判断
    代码看上去清爽点
    '''
    lst.extend(seq1[i:])
    lst.extend(seq2[j:])
    arr[low:high] = lst     #将有序的lst赋值到部分arr

while True:
    try:
        arr = list(map(int,input().strip().split()))
        res = Merge_sort_NotR(arr)
        print(res)
    except EOFError:
        break
















