'''
在英语中，我们有一个叫做 词根(root)的概念，它可以跟着其他一些词组成另一个较长的单词——
我们称这个词为 继承词(successor)。例如，词根an，跟随着单词 other(其他)，可以形成新的单词 another(另一个)。

现在，给定一个由许多词根组成的词典和一个句子。你需要将句子中的所有继承词用词根替换掉。
如果继承词有许多可以形成它的词根，则用最短的词根替换它。

你需要输出替换之后的句子。

示例：

输入：dict(词典) = ["cat", "bat", "rat"] sentence(句子) = "the cattle was rattled by the battery"
输出："the cat was rat by the bat"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/replace-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''

'''

from collections import defaultdict
#字典树节点类
class TrieNode:

    def __init__(self):
        self.end = False
        self.children = defaultdict(TrieNode)

#字典树类
#需要新定义一个函数，用于找到并返回一个单词的前缀
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for c in word:
            node = node.children[c]
        node.end = True

    def search_prefix(self, word: str) -> str:
        """

        :param word: 单词
        :return: 前缀
        """
        prefix = ''
        node = self.root
        for c in word:
            if c not in node.children:
                return ''
            node = node.children[c]
            prefix += c
            if node.end:
                return prefix


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.end


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        注：单词本身也是单词的前缀
        """
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True


class Solution:
    def replaceWords(self, dict: [str], sentence: str) -> str:
        #初始化字典树
        trie = Trie()
        for word in dict:
            trie.insert(word)

        #替换sentence中的目标单词
        sentence_lst = sentence.split()
        for i in range(len(sentence_lst)):
            if trie.search_prefix(sentence_lst[i]):
                sentence_lst[i] = trie.search_prefix(sentence_lst[i])

        res = ' '.join(sentence_lst)
        return res.strip()

#测试
if __name__ == "__main__":
    dict = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"

    res = Solution().replaceWords(dict,sentence)
    print(res)

