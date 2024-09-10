class ListNode():
    def __init__(self,val=0,next = None,prev = None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self) -> str:
        return str(self.val)
    
    

class doublyLinkedList():
    def __init__(self,arr) -> None:
        self.head = None
        self.tail = None
        self.size = 0
        for num in arr:
            nodes = ListNode(num)
            if self.head is None:
                self.head = nodes
                self.tail = self.head
            else:
                nodes.prev = self.tail
                self.tail.next = nodes
                self.tail = self.tail.next
            self.size += 1

    def append(self,data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    
    def printing(self):
        current = self.tail
        while current:
            print(current.val, end=" ")
            current = current.prev

    def delete(self,data):
        current = self.head
        while current:
            if current.val == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                self.size -= 1
                return
            current = current.next
    

arr = [1,2,4,5] 

dll = doublyLinkedList(arr)

# dll.printing()
dll.append(4)
# dll.printing()
dll.delete(5)

dll.printing()









# n1 = ListNode(1)
# n2 = ListNode(2)
# n3 = ListNode(3)
# n4 = ListNode(4)

# n1.next = n2
# n2.next = n3
# n2.prev = n1
# n3.prev = n2
# n3.next = n4
# n4.prev = n3

# head = n4

# while head:
#     print(head.val)
#     head = head.prev


    
    
