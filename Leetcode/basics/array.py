# Creating an array
arr = [1,2,3]

# Appending element to an array O(1)
arr.append(4)
print(arr)

# Deleting last element from array O(1)
arr.pop()
print(arr)

# Returning the element at 1 index O(1)
print(arr[1])

# Searching for an element O(N)
print(1 in arr)

my_list = ["apple", "banana", "cherry", "date"]

for index, element in enumerate(my_list):
    print(f"Index: {index}, Element: {element}")

for count, element in enumerate(my_list, start=1):
    print(f"Count: {count}, Element: {element}")

