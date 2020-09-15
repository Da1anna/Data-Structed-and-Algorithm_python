# -*- coding:utf-8 -*-
# @Time: 2020/9/8 17:14
# @Author: Lj
# @File: 综合版.py

'''

'''
'''
1.冒泡排序
    思路：1.从数组起点开始，比较i和i+1位置的值，将大的交换到后一个，继续遍历，
        直到将最大值交换到数组末尾
         2.重复1，第二次将最大值交换到数组倒数第二位，依次类推
    特点：1.交换次数多，导致操作效率低
          2.可以在程序中设置早停：未发生交换说明数组已有序，可以停止遍历
'''

#原始版
def bubble_sort1(arr):
    for num in range(len(arr)-1,0 ,-1):
        for i in range(num):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]


#加入早停标志
def bubble_sort2(arr):
    end = len(arr)-1
    swap = True
    while end > 0 and swap:
        swap = False
        for i in range(end):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap = True
        end -= 1

#将早停改为交换位置
def bubble_sort3(arr):
    m = len(arr)-1
    while m > 0:
        last_pos = 0
        for i in range(m):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                last_pos = i
        m = last_pos



'''
2.选择排序
    思路：1.从数组起点开始，遍历数组，找出最小值的位置，与数组首位交换；
          2.从第二位开始，重复1；...直到全部有序
    特点：1.算是对冒泡排序的改进，因为每次遍历只发生一次交换
         2.不能早停，因为在中途确定数组已有序与否  
'''

#标准答案
def select_sort(arr):
    for i in range(len(arr)-1):
        min_pos = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_pos]:
                min_pos = j
        arr[i], arr[min_pos] = arr[min_pos], arr[i]


'''
3.插入排序
    思路：1.将数组首位视为有序部分，其余视为无序部分，从无序部分首位开始，与有序部分
        的值比较（从右往左），若小于，则将有序部分的值赋值到后一位，继续与有序部分剩余比较
        ；若大于等于，则将该值赋值到当前位置，停止
         2.遍历无序部分，将无序部分的每个值重复1，直到数组全部是有序部分
    特点：1.没有交换，只有比较、移动（空出）、插入
          2.若数组整体有序，则比较和移动操作会大大减少
            这也导致了它的优化算法——希尔排序  
'''

#标准答案
def insert_sort(arr):
    for i in range(1,len(arr)):
        tmp = arr[i]
        pre_pos = i-1
        while pre_pos >= 0 and tmp < arr[pre_pos]:
            arr[pre_pos+1] = arr[pre_pos]
            pre_pos -= 1
        arr[pre_pos+1] = tmp


'''
4.希尔排序
    思路：希尔排序是对插入排序的改进，利用分治的思想，将待排序数组用gaps间隔数组依次分隔成
        子数组，按照gaps顺序，依次对每个子数组进行插入排序，最后的gap是1，即最后一次是整体
        的插入排序
    特点：1.利用分治的思想和插入排序的特点（整体有序，效率提高），对插入排序进行改进
          2.时间复杂度分析复杂，大致在O(nlog(n))~O(n2)之间
'''

#不调用插入排序
def shell_sort1(arr):
    gaps = [5,3,1]
    for gap in gaps:
        for front in range(gap):
            for i in range(front+gap, len(arr), gap):
                tmp = arr[i]
                pre_pos = i-gap
                while pre_pos >= 0 and tmp < arr[pre_pos]:
                    arr[pre_pos+gap] = arr[pre_pos]
                    pre_pos -= gap
                arr[pre_pos+gap] = tmp

#调用插入排序
def shell_sort2(arr):
    gaps = [5,3,1]
    for gap in gaps:
        for front in range(gap):
            insert_sort2(arr, front+gap, gap)

#带位置参数的插入排序
def insert_sort2(arr, start, gap):
    for i in range(start, len(arr), gap):
        tmp = arr[i]
        pre_pos = i - gap
        while pre_pos >= 0 and tmp < arr[pre_pos]:
            arr[pre_pos + gap] = arr[pre_pos]
            pre_pos -= gap
        arr[pre_pos + gap] = tmp


'''
5.归并排序
    思路：用分治的思想，归并：递归的划分，再合并
        1.递归的将原数组平均分成两部分，直到长度为1（有序了，可以归并）————递归的划分
        2.将有序的小数组合并成一个大数组，直到大到原数组————合并
    特点：1.递归程序不容易写
          2.时间复杂度为O(nlog(n)),空间消耗大，复杂度为O(n)  
'''

#递归版
def merge_sort_R(arr) -> list:
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    arr_l = merge_sort_R(arr[:mid])
    arr_r = merge_sort_R(arr[mid:])
    return _merge(arr_l, arr_r)

def _merge(arr1, arr2) -> list:
    '''合并两个有序数组成一个有序数组'''
    new_arr = []
    i,j = 0,0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            new_arr.append(arr1[i])
            i += 1
        else:
            new_arr.append(arr2[j])
            j += 1
    new_arr.extend(arr2[j:] if j < len(arr2) else arr1[i:])
    return new_arr

'''
非递归版
    与递归版的处理顺序有区别，不是用栈来替代递归
'''
def merge_sort_NR(arr):
    i = 1
    while i < len(arr):
        low = 0
        while low < len(arr):
            mid = low + i
            #python的切片操作对于超出索引的值，取最大索引，所以这里不必担心high超出len()
            high = mid + i
            _merge2(arr, low, mid, high)
            # print(arr)
            low = high
        i *= 2

def _merge2(arr, low, mid, high):
    arr1 = arr[low:mid]
    arr2 = arr[mid:high]
    new_arr = []
    i,j = 0,0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            new_arr.append(arr1[i])
            i += 1
        else:
            new_arr.append(arr2[j])
            j += 1
    new_arr.extend(arr2[j:] if j < len(arr2) else arr1[i:])
    #将有序部分赋值到原数组对应位置
    arr[low:high] = new_arr


'''
6.快速排序
    思路：利用分治的思想，有两种方式：填坑法和左右交换法，下面以填坑法为例
        1.设置中值（一般设数组首位）， 左右标记（尾部和首部），从右标记开始遍历，将小于
          中值的数赋值到左标记；再由左标记开始遍历，将大于中值的数赋值到右标记；最后将
          中值赋值到左右标记（此时它们相等）
        2.递归的执行被中值拆分的子数组  
    特点：1.实际上是最快的最优的排序算法，实际应用最多    
'''

#递归版
def quick_sort_R(arr, low, high):
    if low >= high:
        return
    x = arr[low]
    l, r = low, high
    while l < r:
        while r > l and arr[r] > x:
            r -= 1
        if r > l:
            arr[l] = arr[r]
            l += 1
        while l < r and arr[l] <= x:
            l += 1
        if l < r:
            arr[r] = arr[l]
            r -= 1
    arr[r] = x
    print(arr)
    quick_sort_R(arr, low, r-1)
    quick_sort_R(arr, r+1, high)


#非递归版，用栈储存待排序的上下限位置，但子数组们的排序顺序与递归版不同
def quick_sort_NR(arr):
    stack = []
    stack.append((0,len(arr)-1))
    while stack:
        low, high = stack.pop()
        if low >= high:
            continue
        #下面这一段是对单个数组进行填坑法快排，可以单独写成一个函数，便于理解
        x = arr[low]
        l, r = low, high
        while l < r:
            while r > l and arr[r] > x:
                r -= 1
            if r > l:
                arr[l] = arr[r]
                l += 1
            while l < r and arr[l] <= x:
                l += 1
            if l < r:
                arr[r] = arr[l]
                r -= 1
        arr[r] = x
        print(arr)
        stack.append((low, r-1))
        stack.append((r+1, high))


'''
7.堆排序
    见leetcode\BinaryTree\二叉树的基础.py
'''

#测试
arr = [5,3,4,9,1,8,2,7,6,0]
quick_sort_NR(arr)
print(arr)

