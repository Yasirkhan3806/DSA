class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def find_ancestors(root, target):
    # Initialize an empty list to store ancestors
    ancestors = []
    
    # Traverse the BST to find the target node and track its ancestors
    while root:
        # If the target is smaller, go to the left subtree
        if target < root.val:
            ancestors.append(root.val)
            root = root.left
        
        # If the target is greater, go to the right subtree
        elif target > root.val:
            ancestors.append(root.val)
            root = root.right
        
        # If the target is found, return the list of ancestors
        else:
            return ancestors

    # If the target is not found in the BST, return an empty list
    return []

# Example usage
root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.left.left = Node(5)
root.left.right = Node(15)

target = 15
ancestors = find_ancestors(root, target)
print(f"Ancestors of node {target}: {ancestors}")
