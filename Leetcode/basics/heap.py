# Heap or Priority Queue
# heapq maintains a binary min-heap inside a
# plain list using array indexing math instead of explicit tree nodes.
import heapq

# Create a list
h= [3,1,4]
print(h)

#Convert list to a heap O(n)
heapq.heapify(h)
print(h)

#Push an element to heap O(log n)
heapq.heappush(h, 2)
print(h)

#Pop an element from heap O(log n)
heapq.heappop(h)
print(h)

#Accessing smallest element in a heap O(1)
print(h[0])

heapq.heappop(h)
print(h)
heapq.heappop(h)
print(h)
