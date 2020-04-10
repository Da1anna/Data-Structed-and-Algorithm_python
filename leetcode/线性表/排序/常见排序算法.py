'''
@time:2020/2/27--

'''

'''
1 插入类排序
1.1 直接插入排序
    
'''


def direct_insert_sort1(lst:list):
    '''
    直接插入排序：从左往右比较，先定位，再一起移动
    :param lst:原数组
    :return: 排序后的数组
    '''
    k = len(lst)
    j = 0
    for i in range(1,k):    #遍历无序部分
        temp = lst[i]
        while temp > lst[j]:    #定位
            j += 1
        while i-1 >= j:     #挤空
            lst[i] = lst[i-1]
            i -= 1
        lst[j] = temp   #插入
        j = 0
    return lst


'''
改进：从有序数组的右边向左比，边比较边挤空
'''

def direct_insert_sort2(lst:list):
    '''
    改进版
    :param lst:
    :return:
    '''
    for i in range(1,len(lst)):
        temp = lst[i]
        index = i -1    #从右边开始比较的位置
        while index >= 0 and temp < lst[index]:
            lst[index + 1] = lst[index]
            index -= 1
        lst[index + 1] = temp
    # print(lst)
    return lst

'''
1.2 希尔排序
'''
def Shell_sort(lst:list, increments:list):
    '''
    希尔排序
    :param lst:
    :return:
    '''
    for increment in increments:
        for start in range(increment):
            insert_sort(lst,start,increment)
    return lst

def insert_sort(lst,start,increment):
    '''
    带增量参数的插入排序
    '''
    for i in range(start+increment,len(lst),increment):
        temp = lst[i]
        pos = i - increment
        while pos >= start and temp < lst[pos]:
            lst[pos + increment] = lst[pos]
            pos -= increment
        lst[pos + increment] = temp


'''
2.选择类排序
2.1 简单选择排序
'''
def simple_select_1(lst:list):
    '''
    简单选择排序
    :param lst:
    :return:
    '''
    for i in range(len(lst)):
        index = i + 1       #待比较位置
        temp = lst[i]
        temp_index = i
        #遍历无序组，选出最小值
        while index < len(lst):
            if lst[index] < temp:
                temp = lst[index]
                temp_index = index       #记录最小值的位置，便于后续挤空
            index += 1
        #挤空插入
        j = temp_index
        while j > i:
            lst[j] = lst[j - 1]
            j -= 1
        #插入
        lst[i] = temp
    return lst

'''
改进版：
    1.根本不用挤空，直接将最小值与无序组的首位交换即可
    2.既然定义了min_index，就可以省略temp变量
    3.while循环可以改为for循环
'''
def simple_select_2(lst:list):
    for i in range(len(lst)-1):       #遍历无序数组
        min_index = i     #辅助变量：最小值位置
        #找出最小值的位置
        for j in range(i+1,len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        #最小值和无序组第一位互换位置
        lst[i],lst[min_index] = lst[min_index],lst[i]
    return lst



'''
2.2 归并排序（二路归并）
'''
#递归版
def merge_sort_R(lst:list):
    # 递归边界
    if len(lst) == 1:
        return lst
    #递归模式
    mid = len(lst) // 2
    lst1 = merge_sort_R(lst[:mid])
    lst2 = merge_sort_R(lst[mid:])
    #返回值
    return merge(lst1,lst2)

def merge(lst1,lst2):
    '''
    不用python的pop函数,用辅助变量i，j表示两个有序数组的遍历位置
    :param lst1:
    :param lst2:
    :return:
    '''
    res = []
    i,j = 0,0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            res.append(lst1[i])
            i += 1
        else:
            res.append(lst2[j])
            j += 1
    res.extend(lst1[i:] if i < len(lst1) else lst2[j:])
    return res


#非递归版
# def merge_sort_NR():

'''
3.交换类排序
3.1 冒泡排序
'''

def bubble_sort1(lst:list):
    for i in range(len(lst)-1,0,-1):    #每次需比较的最后一个位置
        j = 0       #每次从左边开始比较
        while j < i:
            if lst[j] > lst[j+1]:
                lst[j+1],lst[j] = lst[j],lst[j+1]
            j += 1
    return lst

'''
改进版：1.改为for循环
        2.更数学化和易理解
'''
def bubble_sort2(lst:list):
    for i in range(1,len(lst)):     #趟数
        for j in range(len(lst)-i):     #遍历要比较的位置
            if lst[j] > lst[j+1]:
                lst[j+1],lst[j] = lst[j],lst[j+1]
    return lst

'''
算法改进版：增加交换位置变量
'''

def bubble_sort3(lst:list):
  m = len(lst)-1
  while m > 0:      #因为比较趟数与pos有关系，所以用while循环不用for
      pos = 0
      for j in range(m):    #比较0到pos
          if lst[j] > lst[j + 1]:
              lst[j + 1], lst[j] = lst[j], lst[j + 1]
              pos = j      #记录最后一次交换的位置
      m = pos      #赋值给m，若没有发生交换（m = 0），则说明数组已有序
  return lst
# lst = [5,3,1,7,9,8,8,6,4]
# res = bubble_sort4(lst)
# print(res)

'''
3.2 快速排序
'''
#递归版
def qksort_R(lst,l:int,h:int):
    '''

    :param lst:
    :param l: 数组首位地址
    :param h: 数组末位地址
    :return:
    '''
    if l >= h:
        return
    i,j = l,h
    x = lst[i]      #这里的枢纽值取的是数组的第一项
    while i < j:
        while i < j and lst[j] > x:
            j -= 1
        if i < j:
            lst[i] = lst[j]
            i += 1
        while i < j and lst[i] < x:
            i += 1
        if i < j:
            lst[j] = lst[i]
            j -= 1
    lst[j] = x
    qksort_R(lst,l,j-1)
    qksort_R(lst,j+1,h)


#非递归版
def qksort_NR(lst,left,right):
    '''
    用栈存取待‘填坑’排序的左右位置
    :param lst:
    :param left:
    :param right:
    :return:
    '''
    stack = []
    if left < right:
        stack.append((left,right))
        while stack:
            i,j = stack.pop()
            index = part_qksort(lst,i,j)
            if index - 1 > i:
                stack.append((i,index-1))
            if index + 1 < j:
                stack.append((index+1,j))


def part_qksort(lst,left,right) -> int:
    '''
    快速排序填坑法
    :param lst:
    :param left:
    :param right:
    :return:
    '''
    i,j = left,right
    x = lst[i]
    while i < j:
        while i < j and lst[j] > x:
            j -= 1
        if i < j:
            lst[i] = lst[j]
            i += 1
        while i < j and lst[i] < x:
            i += 1
        if i < j:
            lst[j] = lst[i]
            j -= 1
    lst[j] = x
    return j


''''''''''''''''''''''''
lst = [6,7,2,3,1,5,9,4,8]   #输入
# lst = list(map(int,input().strip().split()))
# qksort_NR(lst,0,8)
# print(lst)
# print(''.join(str(i) for i in res).strip())















