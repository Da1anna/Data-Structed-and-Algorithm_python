def insert_sort(l,start,increment):
    #正宗的插入排序
    #遍历有序数组后面的未排序数组
    for i in range(start+increment,len(l),increment):
        index = i - increment   #比较的起点
        temp = l[i]
        while l[index] > temp and index >= 0:
            l[index + increment] = l[index]     #比插入值大的值往后移
            index -= increment
        l[index + increment] = temp     #将插入值插到正确的位置
    return l

def shell_sort(l, increments):
    #遍历增量
    for increment in increments:
        # 对增量划分的每一组进行排序
        for i in range(0, increment):
            #简单插入排序
            insert_sort(l, i, increment)

    return l

# 测试
# l = [5, 2, 9, 8, 1, 10, 3, 4, 7]
# increments = [3,2,1]
# print("开始", l)
# l = shell_sort(l, increments)
# print("结束", l)

#题目的输入要求
count = int(input())
for _ in range(count):
    arr = list(map(int,input().split()))
    gaps = list(map(int,input().split()))
    arr_sorted = shell_sort(arr,gaps)
    print(' '.join(str(i) for i in arr_sorted).strip())