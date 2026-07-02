from collections import deque

queue1: deque[int] = deque()

queue1.append(1)
queue1.append(2)
queue1.append(3)

print(queue1)
print(queue1.popleft())
print(queue1)




"""
stack1: list[int] = []

stack1.append(1)
stack1.append(2)
stack1.append(3)

print(stack1)

#stack1.pop()

print(stack1.pop())
"""