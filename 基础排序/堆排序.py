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
        if j+1 <= k and seq[j] < seq[j+1]:  #判断是否有有叶节点且值是否比父节点大
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
    for i in range(n//2-1,-1,-1):
        part_sort(seq,i,n-1)
        print(seq)
    #不断将堆顶元素与数组末尾互换，然后调整剩余位置，使其满足大顶堆堆性质
    for i in range(n-1,-1,-1):
        seq[i],seq[0] = seq[0],seq[i]
        part_sort(seq,0,n-1)    #n-1相当于把选出来的最大值隔离，不再参与建堆

seq = [1,4,2,3,8,9,0,-1,5]

Heap_sort(seq)
print(seq)

'''
第二次理解堆排序
'''
def build_maxHeap(sep,startindex):
    k = len(sep)-1      #最大索引值
    i = startindex
    # temp = seq[i]
    j = 2*i+1   #左叶子节点
    while j <= k:
        #如果有右叶子节点，与左叶子节点进行比较
        if j+1 <=k and seq[j+1] > seq[j]:
            j += 1
        #将较大值与父节点进行比较
        if seq[j] > seq[i]:
            seq[i],seq[j] = seq[j],seq[i]
            #刷新父节点和叶子节点，便于继续向下进行比较
            i = j
            j = 2*i+1
        #子节点不比父节点大的情况，什么都不做
        else:
            break
def heap_sort(seq):
    n = len(seq)
    #从第一个非叶子节点开始（从后往前）建堆
    for i in range(n//2-1,-1,-1):
        build_maxHeap(seq,i)
        print(seq)

    for i in range(n-1,0,-1):
        #交换堆顶值与数组末位值
        seq[0],seq[i] = seq[i],seq[0]
        #将堆顶值移到合适位置，重新构建大顶堆，注意被交换到末位的最大值不再参与建堆
        build_maxHeap(seq[:i],0)
        print(seq)

heap_sort(seq)
print(seq)


























