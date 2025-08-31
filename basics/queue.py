from collections import deque

# Creating a queue
q = deque([1,2])
print(q)

# Appending an element to a queue Enqueue O(1)
q.append(3)
print(q)

# Dequeue O(1)
q.popleft()
print(q)