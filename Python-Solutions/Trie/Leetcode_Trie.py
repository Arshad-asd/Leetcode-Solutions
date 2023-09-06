
                                                     # TRIE LEETCODE SOLUTIONS
'''--------------------------------------------------------------------------------------------'''
# QUESTION NO: 208. Implement Trie (Prefix Tree)

class TrieNode:
   def __init__(self):
       self.children = {}
       self.endOfword = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfword = True
    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfword
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
        


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert(word)
param_2 = obj.search(word)
param_3 = obj.startsWith(prefix)

'''--------------------------------------------------------------------------------------------'''

# QUESTION NO: 211. Design Add and Search Words Data Structure

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(j , root):
            cur = root

            for i in range(j , len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs( i + 1 , child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word
        return dfs(0,self.root)



# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord(word)
param_2 = obj.search(word)

'''--------------------------------------------------------------------------------------------'''
