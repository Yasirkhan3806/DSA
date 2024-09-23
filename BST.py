class Node():
    def __init__(self,data) -> None:
        self.parent = None
        self.left_child = None
        self.right_child = None
        self.data = data

    

class BinaryTree():
    def __init__(self) -> None:
        self.root = None

    def add_node(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
        else:
            current = self.root
            parent = None
            while True:
                parent = current
                if node.data < current.data:
                    current = current.left_child
                    if current is None:
                        parent.left_child = node
                        return
                    
                elif node.data > current.data:
                    current = current.right_child
                    if current is None:
                        parent.right_child = node
                        return
                    
    def get_node_with_parent(self, data):
        parent = None
        current = self.root

        # If the tree is empty, return (None, None)
        if current is None:
            return (parent, None)
        
        # Traverse the tree to find the node
        while current is not None:
            if current.data == data:
                return (parent, current)  # Return parent and current when node is found
            elif current.data > data:
                parent = current
                current = current.left_child  # Move left if the data is smaller
            else:
                parent = current
                current = current.right_child  # Move right if the data is larger

        # If we reach here, the node was not found, return (None, None)
        return (parent, current)
    
    def delete_node(self, data):
        parent, node = self.get_node_with_parent(data)
        
        # Handle the case where the node doesn't exist
        if node is None:
            return False

        children = 0
        
        # First case: node has no children
        if node.left_child is None and node.right_child is None:
            children = 0
        
        # Second case: node has two children
        elif node.left_child and node.right_child:
            children = 2
        else:
            children = 1  # Only one child exists
        
        # Handle the case where the node has no children (leaf node)
        if children == 0:
            if parent:
                if parent.left_child == node:
                    parent.left_child = None
                else:
                    parent.right_child = None
            else:
                # This means the node is the root, so set the root to None
                self.root = None
            return True

        # Handle the case where the node has one child
        elif children == 1:
            child = node.left_child if node.left_child else node.right_child
            if parent:
                if parent.left_child == node:
                    parent.left_child = child
                else:
                    parent.right_child = child
                child.parent = parent
            else:
                # This means the node is the root, so replace the root with the child
                self.root = child
            return True

        # Handle the case where the node has two children
        if children == 2:
            # Find the in-order successor (smallest node in right subtree)
            successor = node.right_child
            parent_of_successor = node
            
            # Move to the leftmost node in the right subtree
            while successor.left_child:
                parent_of_successor = successor
                successor = successor.left_child

            # Replace node's data with successor's data
            node.data = successor.data

            # If the successor has a right child, link it to the parent
            if successor.right_child:
                if parent_of_successor != node:
                    parent_of_successor.left_child = successor.right_child
                else:
                    parent_of_successor.right_child = successor.right_child
            else:
                # If successor has no children, just remove it
                if parent_of_successor != node:
                    parent_of_successor.left_child = None
                else:
                    parent_of_successor.right_child = None

            return True
        
    def search(self,data):
        current = self.root
        
        while current:
            if current.data == data:
                return (data,True)
            elif current.data > data:
                current = current.left_child
            else:
                current = current.right_child
        return (None, False)


binary_tree = BinaryTree()
for num in range(10):
    binary_tree.add_node(num)

# # print(binary_tree.get_node_with_parent(9))

# binary_tree.delete_node(9)

# print(binary_tree.get_node_with_parent(9))

# print(binary_tree.search(9))




    




    
