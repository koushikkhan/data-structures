"""
Implementing trie data structure in Python
"""


# define trie node
class TrieNode:
    """
    Trie node
    """

    def __init__(self, char):
        # take the character to be stored
        self.char = char

        # make provision for other nodes
        self.children = {}

        # keep the node open
        self.is_end = False


class Trie:
    """
    class for trie data structure
    """

    def __init__(self):
        # while initializing this class, it should
        # have a root node and that shouldn't contain
        # any character
        self.root = TrieNode("")

    def insert(self, word):
        # insert a word in the Trie
        print(f"inserting `{word}` in trie ...")
        node = self.root

        for char in word:
            if char in node.children:
                print(f"{char} node is present in trie")

                # update node pointer
                node = node.children[char]
            else:
                print(
                    f"{char} node is not present in trie, I am going to create"
                )
                new_node = TrieNode(char)

                # plugin this node to the parent node
                node.children[char] = new_node

                # update node pointer
                node = node.children[char]

        # mark as end of word
        node.is_end = True

    def search(self, query):
        # make a query to find a word
        print(f"searching for `{query}` ...")
        node = self.root

        for char in query:
            if char in node.children:
                print(f"{char} node is there, looking for next one")
                node = node.children[char]
            else:
                print(f"{query} word is not there in trie")

        # print(f"debug: {node.is_end}")

        if node.is_end:
            print(f"`{query}` word is there in trie")
        else:
            print(f"`{query}` word is not there in trie")


if __name__ == "__main__":
    t = Trie()
    t.insert("mapping")
    print("\n")
    t.insert("man")
    print("\n")
    t.insert("mango")
    print("\n")
    t.search("man")