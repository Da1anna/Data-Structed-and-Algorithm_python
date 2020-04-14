# print([1] + [2] + [2,3])

# lst = [1,2,3]
# print(lst[1:2])

# dict = {'a':1,'b':2}
# # for x in dict:
#     # print(x)
#
# lst = [1,
#        2,
#        3,
#        4,
#        5]
# demo = [1,2]
#
# bol = [1,2,3] in lst
# print(bol)

import sys
print(sys.path)

from leetcode.BinaryTree.NodeAndBuildTree import *

root_lst = [3,5,1,6,2,0,8,None,None,7,4]
root = list_buildTree(root_lst)

g = {}
g[1] = 'a'
print(g[1])

g = {}
def dfs(root):
    if root.left:
        g[root.val].add(root.left.val)
        g[root.left.val] = root.val
        dfs(root.left)
    if root.right:
        g[root.val] = root.right.val
        g[root.right.val] = root.val
        dfs(root.right)
dfs(root)
print(g)

