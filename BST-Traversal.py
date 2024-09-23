# main.py
from BST import BinaryTree
from collections import deque

class ExtendedBinaryTree(BinaryTree):
    # depth first transversal
    def in_order(self, node):
        current = node
        if current is None:
            return 
        self.in_order(current.left_child)
        print(current.data)
        self.in_order(current.right_child)
    def pre_order(self, node):
        current = node
        if current is None:
            return 
        print(current.data)
        self.in_order(current.left_child)
        self.in_order(current.right_child)

    def post_order(self, node):
        current = node
        if current is None:
            return
        self.in_order(current.left_child)
        self.in_order(current.right_child)
        print(current.data)

    # Breadth first Trasversal 
    def breadth_first(self, node):
        queue = []
        list_nodes = []
        queue.append(node)
        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.pop(0)
                if node.left_child:
                    print(node.right_child.data)
                    queue.append(node.right_child)  # Append to queue, not list_nodes
                if node.right_child:
                    print(node.left_child.data)
                    queue.append(node.left_child)  # Append to queue, not list_nodes

        # return list_nodes
        



extendedTree = ExtendedBinaryTree()
for num in range(10):
    extendedTree.add_node(num)

# extendedTree.in_order(extendedTree.root)
# print(extendedTree.breadth_first(extendedTree.root))
extendedTree.breadth_first(extendedTree.root)
