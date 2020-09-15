'''
蛮力法
简单选择排序
'''

def select_sort(arr):
    for i in range(len(arr)-1):
        minindex = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[minindex]:
                minindex = j
        arr[i],arr[minindex] = arr[minindex],arr[i]
    print(arr)
arr = [1,2,8,4,5,7,9,6,3,0]
select_sort(arr)