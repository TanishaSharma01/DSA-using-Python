import bisect
arr = [1, 3, 5, 7]

idx = bisect.bisect_left(arr, 4)   # returns 2 (insert before 5)

print(idx)