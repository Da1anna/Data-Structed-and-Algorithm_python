'''
给出一个字符串数组words组成的一本英语词典。从中找出最长的一个单词，
该单词是由words词典中其他单词逐步添加一个字母组成。若其中有多个可行的答案，则返回答案中字典序最小的单词。

若无答案，则返回空字符串。

示例 1:

输入:
words = ["w","wo","wor","worl", "world"]
输出: "world"
解释:
单词"world"可由"w", "wo", "wor", 和 "worl"添加一个字母组成。
示例 2:

输入:
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
输出: "apple"
解释:
"apply"和"apple"都能由词典中的单词组成。但是"apple"得字典序小于"apply"。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-word-in-dictionary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from leetcode.time_vs import time_this_function
class Solution:

    #排序后筛选
    @time_this_function
    def longestWord_1(self, words: [str]) -> str:
        #将长度为1的单词加入set中：因为set是hash，能加快查询速度
        words_set = set()
        for word in words:
            if len(word) == 1:
                words_set.add(word)
        if not words_set:
            return ''

        res = min(words_set)    #res默认为最靠前的一个字母
        words_sort = sorted(words,key=lambda x:(len(x),x))
        for word in words_sort:
            #单词除去最后一个字母
            word_pre = word[:len(word)-1]
            if word_pre in words_set:
                words_set.add(word)
                if len(word) > len(res):
                    res = word
        return res

#字典树
from collections import defaultdict
class Solution_2:
    def longestWord(self, words: [str]) -> str:
        res=''
        trie=Trie()
        for word in words:
            trie.insert(word)
        for word in words:
            if trie.search(word):
                if len(word) > len(res):
                    res=word
                elif len(word)==len(res) and word < res:
                    res=word
        return res

class TrieNode:
    def __init__(self):
        self.end=False
        self.children=defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        node=self.root
        for s in word:
            node=node.children[s]
        node.end=True

    def search(self, word: str) -> bool:
        node=self.root
        for s in word:
            node=node.children.get(s)
            if node is None or not node.end:
                return False
        return True



#测试
if __name__ == "__main__":
    words = ["ts","e","x","pbhj","opto","xhigy","erikz","pbh","opt","erikzb","eri","erik","xlye","xhig","optoj","optoje","xly","pb","xhi","x","o"]
    res1 = Solution().longestWord_1(words)
    res2 = Solution_2().longestWord(words)
    print(res1,res2)