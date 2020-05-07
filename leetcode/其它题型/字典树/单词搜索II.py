'''
给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
同一个单元格内的字母在一个单词中不允许被重复使用。

示例:

输入:
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

输出: ["eat","oath"]
说明:
你可以假设所有输入都由小写字母 a-z 组成。

提示:

你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？
如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。
什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？
前缀树如何？如果你想学习如何实现一个基本的前缀树，请先查看这个问题： 实现Trie（前缀树）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-search-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from leetcode.其它题型.字典树.Trie import Trie
class Solution:

    #时间击败了9%！！！
    def findWords(self, board: [[str]], words: [str]) -> [str]:
        #将words加入字典树
        trie = Trie()
        for word in words:
            trie.insert(word)

        #dfs函数
        def dfs(i, j, cur, board):
            if not trie.startsWith(cur):
                return
            if trie.search(cur):
                res.append(cur)
                # return        #这里找到一个单词时，不能停止函数，因为还可能以此为前缀的单词
            tmp = board[i][j]
            board[i][j] = '#'
            for (x,y) in [(i-1,j),(i,j-1),(i+1,j),(i,j+1)]:
                if -1 < x < m and -1 < y < n and board[x][y] != '#':
                    dfs(x, y, cur + board[x][y], board)
            board[i][j] = tmp

        #遍历board上的字母
        m,n = len(board),len(board[0])
        # board = [[False for _ in range(n)] for _ in range(m)]
        res = []
        for i in range(m):
            for j in range(n):
                #DFS
                cur = board[i][j]
                dfs(i,j,cur,board)
        res_ = list(set(res))
        return sorted(res_)

#测试
if __name__ == "__main__":
    board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
    words = ["oath","pea","eat","rain"]
    res = Solution().findWords(board,words)
    print(res)