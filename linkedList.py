class Node:
    def __init__(self,data) :
        self.data = data
        self.next = None
    

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
    # def size(self):
    #     count = 0
    #     current = self.head
    #     while current:
    #         count += 1
    #         current = current.next
    #     return count

        # if self.tail == None:
        #     self.tail = node
        # else:
        #     current = self.tail
        #     while current.next:
        #         current = current.next
        #     current.next = node
    def delete(self,data):
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                else:
                    prev.next = current.next 
                self.size -= 1
                return
            
            prev = current
            current = current.next

    def search(self,data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    def clear(self):
        self.head = None
        self.tail = None



words = singlyLinked()
words.append('egg')
words.append('ham')
words.append('spam')

# words.delete('ham')
head = words.head
while head:
    print(head.data)
    head = head.next
# print(words.size())
words.delete('ham')
print(words.size)
print(words.search('egg'))
words.clear()
while head:
    print(head.data)
    head = head.next

# n1 = Node("sum")
# n2 = Node("lum")
# n3 = Node("bum")

# n1.next = n2
# n2.next = n3

# head = n1
# while head:
#     print(head.data)
#     head = head.next