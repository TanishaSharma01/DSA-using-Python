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

d.update({"e":5})
print(d)

#Default dict
# we dont need to do the following anymore
# Suppose you want to build connections like this:
#
# 1 → 2
# 1 → 3
# 2 → 4
#
#
# Using defaultdict(list):
#
# adj = defaultdict(list)
# adj[1].append(2)
# adj[1].append(3)
# adj[2].append(4)
#
# print(adj)
#
#
# Output:
#
# defaultdict(<class 'list'>, {1: [2, 3], 2: [4]})
#
#
# Without it, you’d have to check for keys every time:
#
# adj = {}
# if 1 not in adj:
#     adj[1] = []
# adj[1].append(2)