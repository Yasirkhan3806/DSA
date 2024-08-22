from collections import deque

stack = deque()

# for i in range(10):
#     stack.append(i)

strinf = "i am gay"
for i in range(len(strinf)):
    stack.append(strinf[i])
stack.reverse()
print(stack)
string = ''
for i in range(len(stack)):
    string += stack[i]

print(string)