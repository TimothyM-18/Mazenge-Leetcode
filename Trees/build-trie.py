# Design a data structure that efficiently stores and retrieves strings. Specifically, 
# implement a Trie (Prefix Tree) with the following operations:

# insert(String word): Inserts a string word into the trie.
# search(String word): Returns true if the string word is present in the trie (i.e., was inserted before), and false otherwise.
# startsWith(String prefix): Returns true if there is any string in the trie that starts with the given prefix, and false otherwise.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, prefix):
        node = self.root

        for ch in prefix:
           if ch not in node.children:
               return False
           node = node.children[ch]
        return node.is_end

    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

trie = Trie()
trie.insert("apple")

print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))

trie.insert("app")
print(trie.search("app"))
    