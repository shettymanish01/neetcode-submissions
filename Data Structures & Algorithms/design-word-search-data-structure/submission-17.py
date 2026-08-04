class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:

        def find(root, j):
            cur = root
            count = j
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for n in cur.children.values():
                        if find(n, i+1):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                
                    cur = cur.children[c]
                    count += 1
            
            if count == len(word) and cur.end:
                return True
            else:
                return False

        return find(self.root,0)

