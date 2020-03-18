'''
插入排序
输入一个用空格隔开的整数类型的数组
输出排好序的用空格隔开的字符串
'''

def Insert_sort(arr):
    '''
    这个方法是将temp值从右往左比较，比较一个移动一个
    :param arr:
    :return:
    '''
    for i in range(1,len(arr)):  #无序数组的遍历
        temp =  arr[i]
        index = i - 1   #比较的位置
        while index >= 0 and arr[index] > temp:     #边比较边往后移
            arr[index+1] = arr[index]
            index -= 1
        arr[index+1] = temp  #最终插入的位置
    return arr
arr = list(map(int,input().strip().split()))
res = Insert_sort(arr)
print(res)
#将格式转换为题目要求的格式
print(' '.join(str(i) for i in res).strip())
# res_str = ''
# for i in res:
#     res_str += str(i)+' '
# print(res_str.strip())