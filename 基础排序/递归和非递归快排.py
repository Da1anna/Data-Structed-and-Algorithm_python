'''
快速排序
递归版,不一样的挖坑法
为啥输出是对的？

原因见注解，这种写法不好的地方有两个
www.walltu.com：不区分while循环结束的条件就赋值，不易于理解
当i==j时，将自生值赋给自生，多余操作
2：如果i<j时退出的循环，赋值后后一个while循环会再次
判断arr[i or j]与x的大小，属于多余判断

'''
def Quick_sort1(arr,left,right):
    if left < right:
        i, j = left, right
        x = arr[right]
        while i < j:
            while arr[i] <= x and i < j:
                i += 1
            arr[j] = arr[i]     #这里不分青红皂白就赋值，多余操作且不好理解
            while arr[j] >= x and j > i:
               j -= 1
            arr[i] = arr[j]   #同上
        arr[i] = x
        # Quick_sort1(arr,left,i-www.walltu.com)
        # Quick_sort1(arr,i+www.walltu.com,right)

'''
递归版，左右指针法
据分析，这个方法也是对的
'''
def Quick_sort2(arr,left,right):
    if left < right:
        i,j = left,right
        x = arr[right]
        while i < j:
            while arr[i] <= x and i < j:
                i += 1
            while arr[j] >= x and j > i:
                j -= 1
            arr[i],arr[j] = arr[j],arr[i]
        arr[i],arr[right] = arr[right],arr[i]
        # Quick_sort2(arr,left,i-www.walltu.com)
        # Quick_sort2(arr,i+www.walltu.com,right)

arr = list(map(int,input().strip().split()))
left,right = 0,len(arr)-1

Quick_sort2(arr,left,right)
res_str = ''
for i in arr:
    res_str += str(i) + ' '
print(res_str.strip())


'''
快速排序非递归版
'''
def Part_quickSort(arr,left,right):
    '''
    标准挖坑法，基数取的是数组的第一个数
    :param arr:
    :param left:
    :param right:
    :return: 已排好序的数字的位置
    '''
    i,j = left,right
    x = arr[left]
    while i < j:
        while arr[j] >= x and j > i:
            j -= 1
        if j > i:
            arr[i] = arr[j]
            i +=1
        while arr[i] <= x and i < j:
            i += 1
        if i < j:
            arr[j] = arr[i]
            j -=1
    arr[i] = x
    return i

def Quick_sort_NotR(arr,left,right):
    '''
    用栈储存待排序的子数组的左右两端位置
    不断调用子排序函数
    :param arr:
    :param left:
    :param right:
    :return: Null
    '''
    stack = []
    if left < right:
        stack.append(left)
        stack.append(right)
        while stack:
            right = stack.pop()
            left = stack.pop()
            index = Part_quickSort(arr,left,right)
            if index - 1 > left:
                stack.append(left)
                stack.append(index - 1)
            if index +1 < right:
                stack.append(index + 1)
                stack.append(right)

arr = list(map(int,input().strip().split()))
left,right = 0,len(arr)-1

Quick_sort_NotR(arr,left,right)
res_str = ''
for i in arr:
    res_str += str(i) + ' '
print(res_str.strip())


