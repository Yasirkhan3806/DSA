class TreeNode():
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    # def add_child(self,data):
    #     data.parent = self


def main():
    rootNode = TreeNode("rootNode")
    leftchild = TreeNode("leftchild")
    rightchild = TreeNode("rightchild")
    leftGrandChild = TreeNode("leftGrandchild")

    rootNode.left = leftchild
    rootNode.right = rightchild
    leftchild.left = leftGrandChild

    current = rootNode
    while current:
        print(current.data)
        current = current.right
main()

