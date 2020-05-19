'''
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-a-2d-matrix-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:

    #逐行二分查找，可以早停
    #时间复杂度：m *（log N）
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m,n = len(matrix),len(matrix[0])
        for i in range(m):
            if matrix[i][0] > target:
                return False
            l,r = 0,n-1
            while l <= r:
                mid = (l + r)//2
                if target == matrix[i][mid]:
                    return True
                elif target < matrix[i][mid]:
                    r = mid-1
                else:
                    l = mid + 1
        return False

    #从左下角开始遍历:时间复杂度——（O（m+n））
    def searchMatrix_2(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m,n = len(matrix),len(matrix[0])
        x_,y_ = m-1,0   #遍历起点
        while x_ >= 0 and y_ < n:
            if matrix[x_][y_] > target:
                x_ -= 1
            elif matrix[x_][y_] < target:
                y_ += 1
            else:
                return True
        return False


#测试
matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
res = Solution().searchMatrix_2(matrix,12)
print(res)