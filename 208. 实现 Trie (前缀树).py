class Trie:
    def __init__(self):
        # 初始化 Trie 的根节点
        self.root = {}  # 使用字典表示节点
        self.end_symbol = "*"  # 表示单词结束的特殊标志

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            # 如果当前字符不在节点中，创建一个新的子节点
            if char not in node:
                node[char] = {}
            # 移动到当前字符对应的子节点
            node = node[char]
        # 插入完成后，在最后一个节点标记单词结束
        node[self.end_symbol] = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            # 如果字符不在当前节点中，返回 False
            if char not in node:
                return False
            # 移动到下一个字符对应的节点
            node = node[char]
        # 检查当前节点是否标记为单词结束
        return self.end_symbol in node

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            # 如果字符不在当前节点中，返回 False
            if char not in node:
                return False
            # 移动到下一个字符对应的节点
            node = node[char]
        # 如果成功遍历完整个前缀，返回 True
        return True
