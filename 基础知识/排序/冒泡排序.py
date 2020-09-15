'''
冒泡排序
输入一个用空格隔开的整数类型的数组
输出排好序的用空格隔开的字符串
'''

#这是最简单版的冒泡
def Bubble_sort(lst):
    for i in range(1,len(lst)):     #趟数
        for j in range(len(lst)-i):     #要比较的位置
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    return lst


lst = list(map(int,input("请输入一个数组：").strip().split()))
res = Bubble_sort(lst)
# res_str = ''
# for i in res:
#     res_str += str(i) + ' '
# print(res_str.strip())
print(' '.join(str(i) for i in res).strip())