'''
堆排序
非递归版

'''
def part_sort(seq,startindex,k):
    '''
    调整单个点，并将其调整到最终位置
    :param seq: 初始数组
    :param startindex: 起始索引位置
    :param k: 数组长度
    :return: 空
    '''
    i = startindex    #父节点位置
    j = 2*i+1         #左叶节点位置
    tmp = seq[i]
    while j <= k:   #叶节点在长度范围内
        if j+1 <= k and seq[j] < seq[j+1]:  #判断是否有右叶节点且值是否比父节点大
            j += 1
        if seq[j] > tmp:    #判断父节点与较大的节点哪个值大
            seq[i] = seq[j]     #将较大值赋给父节点
            #赋值后，刷新父节点和左叶节点位置，便于继续判断
            i = j
            j = 2*i+1
        else:
            break
    seq[i] = tmp
def Heap_sort(seq):
    '''
    主函数
    :param seq:初始数组
    :return: 空
    '''
    n = len(seq)

    #从数组的最后一个非叶节点开始，不断调整，循环结束后，大顶堆建成
    for i in range(n//2-1,-1,-1):   #n//2-1是最后一个节点的父节点
        part_sort(seq,i,n-1)
    print('大顶堆：',seq)

    #不断将堆顶元素与数组末尾互换，然后调整剩余位置，使其满足大顶堆堆性质
    for j in range(n-1,-1,-1):
        seq[j],seq[0] = seq[0],seq[j]
        part_sort(seq,0,j-1)    #n-1相当于把选出来的最大值隔离，不再参与建堆
    print('排序后：',seq)

    return seq


'''
第二次理解堆排序
与前面相比有两点变化：
1.传入形参lst后，实参seq = [0] + lst，取排序的seq索引为1-n,这样便于计算
2.建堆参数不一样，比前面少一个
'''
def build_maxHeap(seq,startindex):
    n = len(seq) - 1    #末位索引
    i = startindex
    j = 2*i   #左叶子节点
    while j <= n:
        #如果有右叶子节点，与左叶子节点进行比较
        if j+1 <= n  and seq[j+1] > seq[j]:
            j += 1
        #将较大值与父节点进行比较
        if seq[j] > seq[i]:
            seq[i],seq[j] = seq[j],seq[i]
            #刷新父节点和叶子节点，便于继续向下进行比较
            i = j
            j = 2*i
        #子节点不比父节点大的情况，什么都不做
        else:
            break
def heap_sort(lst):
    #建堆
    seq = [0] + lst
    n = len(seq) - 1
    #从第一个非叶子节点开始（从后往前）建堆
    for i in range(n//2,0,-1):
        build_maxHeap(seq,i)
    print('大顶堆：',seq[1:])

    #排序
    res = []
    for i in range(n,1,-1):
        #交换堆顶值与数组末位值
        seq[1],seq[i] = seq[i],seq[1]
        res.append(seq.pop())
        build_maxHeap(seq,1)
    res.append(seq.pop())

    # print('排序后：',res)
    return res

lst = [3,1,2,4,5]
print(heap_sort(lst))

























