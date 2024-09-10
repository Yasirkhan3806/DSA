# class queue:
#   def __init__(self):
#     self.queue = []

#   def enqueue(self, item):
#     # self.queue.append(item) # both implementations are correct
#     self.queue.insert(0,item)

#   def dequeue(self):
#     if not self.isEmpty():
#       return self.queue.pop() #both implement are correct 
#         # return self.queue.pop(0)

#     else:
#       return ("Queue is empty")

#   def isEmpty(self):
#     # Check if the queue is empty by checking the length of the list
#     return len(self.queue) == 0
        
# queue = queue()
# for item in range(0,10):
#         queue.enqueue(item)

# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
    

# TWO STACKS METHOD
# class Queue():
#     def __init__(self):
#         self.inboundstack = []
#         self.outboundstack = []

#     def enqueue(self,data):
#         self.inboundstack.append(data)

#     def dequeue(self):
#         if not self.outboundstack:
#             while self.inboundstack:
#                 self.outboundstack.append(self.inboundstack.pop())
#         return self.outboundstack.pop()
    

# queue = Queue()
# for item in range(0,10):
#         queue.enqueue(item)

# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())

# USING DOUBLY lINKEDLIST

class ListNode():
    def __init__(self,val=0,next = None,prev = None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self) -> str:
        return str(self.val)

class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self,data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.size == 1:
            self.head = None
            self.tail = None
        elif self.size > 1:
            self.head = self.head.next
            self.head.prev= None
        self.size -= 1
    def printing(self):
        current = self.head
        while current:
            print(current.val, end=" ")
            current = current.next


queue = Queue()
for num in range(1, 10):
    queue.enqueue(num)

queue.printing()

for num in range(1,4):
    queue.dequeue()

queue.printing()




