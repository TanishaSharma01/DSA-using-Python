# Best case : O(n)
# Worst case : O(log n)

arr = [("a",2) ,("b", 1)]

arr = sorted(arr, key=lambda x: x[1])

print(arr)

