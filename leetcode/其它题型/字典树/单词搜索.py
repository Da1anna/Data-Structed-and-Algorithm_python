'''
设计一个支持以下两种操作的数据结构：

void addWord(word)
bool search(word)
search(word) 可以搜索文字或正则表达式字符串，字符串只包含字母 . 或 a-z 。 . 可以表示任何一个字母。

示例:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
说明:

你可以假设所有单词都是由小写字母 a-z 组成的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-and-search-word-data-structure-design
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
思路：用典型的字典树来考虑，不太好处理‘.’这个通配符，递归（dfs）比较好处理
        所以需要另写一个match函数来递归的搜索，search来调用它
'''
from collections import defaultdict
class TrieNode:

    def __init__(self):
        self.end = False
        self.children = defaultdict(TrieNode)

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for c in word:
            node = node.children[c]
        node.end = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        node = self.root
        return self.match(node,word,0)

    def match(self,node,word,index) -> bool:
        '''
        单独定义一个函数，便于递归处理
        '''
        if len(word) == index:
            return node.end

        c = word[index]
        if c == '.':
            for key in node.children:
                if self.match(node.children[key],word,index+1):
                    return True
            return False
        else:
            if c not in node.children:
                return False
            return self.match(node.children[c],word,index+1)
