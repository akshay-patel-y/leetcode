class Trie:
    
    def __init__(self):
        self.store = set()

    def insert(self, word: str) -> None:
        if word in self.store:
            return True
        self.store.add(word)
        return False

    def search(self, word: str) -> bool:
        return word in self.store
        

    def startsWith(self, prefix: str) -> bool:
        for i in self.store:
            if i.startswith(prefix):
                return True
        return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)