
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert(node.right, value)

    def display(self):
        levels = []
        self._get_levels(self.root, 0, levels)
        for level in levels:
            print(" ".join(str(node.value) for node in level))

    def _get_levels(self, node, depth, levels):
        if node is None:
            return
        if len(levels) <= depth:
            levels.append([])
        levels[depth].append(node)
        self._get_levels(node.left, depth + 1, levels)
        self._get_levels(node.right, depth + 1, levels)

bt = BinaryTree()
bt.insert(10)
bt.insert(5)
bt.insert(15)
bt.insert(3)
bt.insert(7)
bt.insert(12)
bt.insert(18)

print("Binary Tree:")
bt.display()
