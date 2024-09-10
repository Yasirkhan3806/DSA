class Node:
    def __init__(self,data) :
        self.data = data
        self.next = None

class Node:#+
    def __init__(self, data):#+
        """#+
        Initialize a new node with given data.#+
#+
        Parameters:#+
        data (any): The data to be stored in the node.#+
#+
        Attributes:#+
        data (any): The data stored in the node.#+
        next (Node): The next node in the linked list.#+
        prev (Node): The previous node in the linked list.#+
        """#+
        self.data = data#+
        self.next = None#+
        self.prev = None#+
#+
    def __str__(self) -> str:#+
        """#+
        Return a string representation of the node's data.#+
#+
        Returns:#+
        str: The string representation of the node's data.#+
        """#+
        return str(self.data)#+
#+
#+
class singlyLinked:#+
    def __init__(self):#+
        """#+
        Initialize a new singly linked list.#+
#+
        Attributes:#+
        tail (Node): The last node in the linked list.#+
        head (Node): The first node in the linked list.#+
        size (int): The number of nodes in the linked list.#+
        """#+
        self.tail = None#+
        self.head = None#+
        self.size = 0#+
#+
    def append(self, data):#+
        """#+
        Append a new node with the given data to the end of the linked list.#+
#+
        Parameters:#+
        data (any): The data to be stored in the new node.#+
#+
        Attributes:#+
        size (int): Incremented by 1 after appending a new node.#+
        """#+
        self.size += 1#+
        node = Node(data)#+
        if self.head:#+
            self.tail.next = node#+
            self.tail = node#+
        else:#+
            self.tail = node#+
            self.head = node#+
#+
    def creatingList(self, arr):#+
        """#+
        Create a new singly linked list by appending nodes with data from the given array.#+
#+
        Parameters:#+
        arr (list): The array of data to be stored in the new nodes.#+
#+
        Attributes:#+
        size (int): Updated to the length of the given array after creating the linked list.#+
        """#+
        for data in arr:#+
            self.append(data)#+
#+
        # self.head.prev = self.tail.next#+
        self.tail.next = self.head#+    

    def __str__(self) -> str:
        return str(self.data)
    
class singlyLinked:
    def __init__(self) -> None:
        self.tail = None
        self.head = None
       
        self.size = 0
    def append(self,data):
        self.size += 1
        node = Node(data)
        if self.head:
            self.tail.next = node
            self.tail = node
        else:
            self.tail = node
            self.head = node
         
    def creatingList(self, arr):
        for data in arr:
            self.append(data)
        self.tail.next = self.head
