'''
1.给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/balanced-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
2.求二叉树的最大深度

给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class TreeNode():
    '''
    定义树的节点
    '''
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    def height(self,root:TreeNode):
        if not root:
            return 0
        return 1 + max(self.height(root.left),self.height(root.right))

#测试用例是：[3,9,20,null,null,15,7]，不知怎么将数组转换为一颗树？
'''
3.给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-depth-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
class Solution():
    def minDepth(self, root: TreeNode) -> int:
        #若当前节点为空
        if not root:
            return 0
        left_height = self.minDepth(root.left)
        right_height = self.minDepth(root.right)
        #若当前节点有左右子树
        if left_height and right_height:
            return 1 + min(left_height,right_height)
        #若当前节点不同时有左子树和右子树
        else:
            return 1 + left_height + right_height


'''
4.输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，
则最小的4个数字是1、2、3、4。

示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]

限制：

0 <= k <= arr.length <= 10000
0 <= arr[i] <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
可以用堆排序的方法解决
'''
def tiaozheng(lst:list,startindex):
    k = len(lst) - 1
    i = startindex
    j = 2*i + 1
    while j <= k:
        if j + 1 <= k and lst[j+1] < lst[j]:
            j += 1
        if lst[j] < lst[i]:
            lst[i],lst[j] = lst[j],lst[i]
            i = j
            j = 2*j + 1
        else:
            break
def build_heap(lst:list):
    '''

    :param lst: 初始数组
    :param k: 取前k个值
    '''
    #初始化小顶堆
    n = len(lst)
    for i in range(n//2-1,-1,-1):
        tiaozheng(lst,i)
    print("小顶堆：" ,lst)

def topk(lst,k):
    build_heap(lst)     #初始化小顶堆
    top_k = []
    for _ in range(k):
        lst[0],lst[-1] = lst[-1],lst[0]
        top_k.append(lst.pop())
        tiaozheng(lst,0)    #重新调整，注意这里只用将数lst[0]一个数调整到合适位置
    return top_k


# lst = [3,8,9,0,12,5,7,60,1,25,43]
# print(topk(lst,5))


'''
5.给一非空的单词列表，返回前 k 个出现次数最多的单词。

返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率，按字母顺序排序。

示例 1：

输入: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
输出: ["i", "love"]
解析: "i" 和 "love" 为出现次数最多的两个单词，均为2次。
    注意，按字母顺序 "i" 在 "love" 之前。
 

示例 2：

输入: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
输出: ["the", "is", "sunny", "day"]
解析: "the", "is", "sunny" 和 "day" 是出现次数最多的四个单词，
    出现次数依次为 4, 3, 2 和 1 次。
 

注意：

假定 k 总为有效值， 1 ≤ k ≤ 集合元素数。
输入的单词均由小写字母组成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/top-k-frequent-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import collections

def topKFrequent(words,k):
    #统计词频
    dicts = {}
    for word in words:
        if word in dicts:
            dicts[word] += 1
        else:
            dicts[word] = 1
    #对字典进行排序：先转换为可迭代的“元组列表”，再排序
    # print(dicts)
    dists = sorted(dicts.items(), key=lambda x: (-x[1], x[0]))
    # print(dists)
    #取前K个
    res = []
    for key,_ in dists[:k]:
        res.append(key)
    return res

# words = ['q','w','e','r','q','w','q']
# print(topKFrequent(words,2))

























