import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.left, self.right = None, None

class alptree(Node):
    def __init__(self):
        self.root = Node('A')
        self.root.left, self.root.right = None, None
    
    def alpinsert(self, data, left, right):
        self.root = self._alpinsert_value(self.root, data, left, right)
        return self.root is not None

    def _alpinsert_value(self, node, data, left, right):
        if data == node.data:
            node = Node(data)
            node.left, node.right = left, right
            if left:
                node.left = Node(left)
                node.left.left, node.left.right = None, None
            if right:
                node.right = Node(right)
                node.right.left, node.right.right = None, None
        else:
            if node.left:
                node.left = self._alpinsert_value(node.left, data, left, right)
            if node.right:
                node.right = self._alpinsert_value(node.right, data, left, right)
        return node

    def preorder(self, node):
        print(node.data, end='')
        if node.left:
            self.preorder(node.left)
        if node.right:
            self.preorder(node.right)
            
    def inorder(self, node):
        if node.left:
            self.inorder(node.left)
        print(node.data, end='')
        if node.right:
            self.inorder(node.right)
            
    def postorder(self, node):
        if node.left:
            self.postorder(node.left)
        if node.right:
            self.postorder(node.right)
        print(node.data, end='')


def main():
    N = int(input())
    tree = alptree()
    for _ in range(N):
        data, left, right = list(input().split())
        if left == '.':
            left = None
        if right == '.':
            right = None
        tree.alpinsert(data, left, right)

    tree.preorder(tree.root)
    print()
    tree.inorder(tree.root)
    print()
    tree.postorder(tree.root)
    print()

main()

"""

7
A B C
B D .
C E F
E . .
F . G
D . .
G . .

"""