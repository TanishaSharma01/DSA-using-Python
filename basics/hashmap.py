# Creating a hashmap (dictionary)
d = {"a":1, "b":2}

# Adding an element to dictionary O(1)
d["c"] = 3
print(d)

# Getting an element
print(d.get("a"))         # O(1)

# If the key were missing,
# it would return the provided default (0 here) instead of raising a KeyError
print(d.get("e", 0))      # O(1)