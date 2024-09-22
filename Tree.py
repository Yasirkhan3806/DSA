# class TreeNode():
#     def __init__(self,data) -> None:
#         self.data = data
#         self.children = []
#         self.parent = None

#     def addChild(self,child):
#         child.parent = self
#         self.children.append(child)

#     def printingTree(self):
#         spaces = " " * self.get_level() *  2
#         print(spaces,self.data)
        
#         if self.children:
#             for child in self.children:
#                 child.printingTree()

#     def get_level(self):
#         level = 0
#         p = self.parent

#         while p:
#             level += 1
#             p = p.parent
#         return level


# def getElectronicsTree():
#     root = TreeNode('Electronics')

#     laptop = TreeNode('Laptop')
#     laptop.addChild(TreeNode('Macbook'))
#     laptop.addChild(TreeNode('Windows Laptop'))

#     mobile = TreeNode('Mobile')
#     mobile.addChild(TreeNode('iPhone'))
#     mobile.addChild(TreeNode('Android'))

#     node1.addChild(laptop)
#     node1.addChild(mobile)
#     return root
    

# if __name__ == '__main__':
#     root =  getElectronicsTree()
#     node1.printingTree()


class treeNode():
    def  __init__(self,data) -> None:
        self.data = data
        self.parent = None
        self.children = []


    def addChild(self,child):
        child.parent = self
        self.children.append(child)

    def assign_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def printing(self):
        spaces = " " * self.assign_level() * 3
        print(spaces, self.data)
        if self.children:
            for child in self.children:
                child.printing()

    

def createTree():
    root = treeNode('Root node')
    node1 = treeNode(' Node1')
    node2 = treeNode(' Node2')
    # node3 = treeNode(' Node3')
    # node4 = treeNode(' Node4')

    child1node = node1.addChild(treeNode(' Node1 child 1'))
    child2node = node1.addChild(treeNode(' Node1 child 2'))
    child3node = node1.addChild(treeNode(' Node1 child 3'))
    child4node = node1.addChild(treeNode(' Node1 child 4'))

    child1node2 = node2.addChild(treeNode(' Node2 child 1'))
    child2node2 = node2.addChild(treeNode(' Node2 child 2'))
    root.addChild(node1)
    root.addChild(node2)
    return root



if __name__ == '__main__':
    root = createTree()
    root.printing()
    pass
    
